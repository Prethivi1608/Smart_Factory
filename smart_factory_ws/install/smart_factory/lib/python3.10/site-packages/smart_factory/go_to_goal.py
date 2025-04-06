import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist,Point,Quaternion
import math

class Navigation(Node):
    def __init__(self):
        super().__init__('go_to_goal')
        
        self.pos_topic = '/TB3_1/odom'
        self.vel_topic = '/TB3_1/cmd_vel'
        self.pos_sub = self.create_subscription(Odometry,self.pos_topic,self.odom_callback,10)
        self.velocity_pub = self.create_publisher(Twist,self.vel_topic,10)
        self.timer = self.create_timer(1.0,self.velocity_callback)
        self.goal = [3,4]
        self.position = Point()
        self.orientation = Quaternion()
        
    def odom_callback(self,msg):
        
        self.position = msg.pose.pose.position
        self.orientation = msg.pose.pose.orientation
        
    def velocity_callback(self):
        
        angle_to_goal = math.atan2((self.goal[1]-self.position.y),(self.goal[0]-self.position.x))
        angle_to_goal_deg = math.degrees(angle_to_goal)
        
        self.velocity_msg = Twist()
        if angle_to_goal_deg > 0.5:
            if angle_to_goal > 0.0:
                self.velocity_msg.angular.z = 0.5
                self.velocity_pub.publish(self.velocity_msg)
            else:
                self.velocity_msg.linear.x = 0.1
                self.velocity_msg.angular.z = -0.1
                self.velocity_pub.publish(self.velocity_msg)
        else:
            self.velocity_msg.linear.x = 0.0
            self.velocity_msg.angular.z = 0.0
            self.velocity_pub.publish(self.velocity_msg)
                

def main():
    rclpy.init()
    go_goal = Navigation()
    rclpy.spin(go_goal)
    go_goal.destroy_node()
    rclpy.shutdown()
    

