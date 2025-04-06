import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist,Point,Quaternion
import math
import time

class Navigation(Node):
    def __init__(self):
        super().__init__('go_to_goal')
        
        self.pos_topic = '/TB3_2/odom'
        self.vel_topic = '/TB3_2/cmd_vel'
        self.pos_sub = self.create_subscription(Odometry,self.pos_topic,self.odom_callback,10)
        self.velocity_pub = self.create_publisher(Twist,self.vel_topic,10)
        self.timer = self.create_timer(1.0,self.go_to_goal)
        self.goal = [5,2]
        self.position = Point()
        self.orientation = Quaternion()
        
    def odom_callback(self,msg):
        
        self.position = msg.pose.pose.position
        self.orientation = msg.pose.pose.orientation
        
    def get_yaw(self):
        orientation_q = self.orientation
        siny_cosp = 2 * (orientation_q.w * orientation_q.z + orientation_q.x * orientation_q.y)
        cosy_cosp = 1 - 2 * (orientation_q.y**2 + orientation_q.z**2)
        yaw = math.atan2(siny_cosp, cosy_cosp)
        return yaw
        
    def align_to_goal(self):
        
        yaw = self.get_yaw()
        angle_to_goal = math.atan2((self.goal[1]-self.position.y),(self.goal[0]-self.position.x))
        angle_to_goal_deg = math.degrees(angle_to_goal)
        align_goal = angle_to_goal - yaw
        
        self.velocity_msg = Twist()
        if align_goal > 0:
            if abs(align_goal) > 0.05:
                self.velocity_msg.angular.z = -0.2
            else:
                self.velocity_msg.angular.z = 0.0
                self.velocity_pub.publish(self.velocity_msg)
            
            self.velocity_pub.publish(self.velocity_msg)   
        
        else:
            if abs(align_goal) > 0.05:
                self.velocity_msg.angular.z = 0.2
            else:
                self.velocity_msg.angular.z = 0.0
                self.velocity_pub.publish(self.velocity_msg)
            
            self.velocity_pub.publish(self.velocity_msg)
            
    def move_to_goal(self):
        distance = math.sqrt(((self.goal[1]-self.position.y)**2)+((self.goal[0]-self.position.x)**2))
        print(distance)
        
        if distance > 0.5:
            self.velocity_msg.linear.x = 0.5
        else:
            self.velocity_msg.linear.x = 0.0
            
        
        self.velocity_pub.publish(self.velocity_msg)
        
    def go_to_goal(self):
        self.align_to_goal()
        self.move_to_goal() 
        
                

def main():
    rclpy.init()
    go_goal = Navigation()
    rclpy.spin(go_goal)
    go_goal.destroy_node()
    rclpy.shutdown()
    

