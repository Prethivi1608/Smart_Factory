import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist,Point,Quaternion
import math
import time
import numpy as np

class Navigation(Node):
    def __init__(self):
        super().__init__('go_to_goal')
        
        self.pos_topic = '/odom'
        self.vel_topic = '/cmd_vel'
        self.pos_sub = self.create_subscription(Odometry,self.pos_topic,self.odom_callback,10)
        self.vel_pub = self.create_publisher(Twist,self.vel_topic,10)

        
    def odom_callback(self,msg):

        vel_msg = Twist()
        angular_vel = 0.1
        goal_position = [1,2]

        position = msg.pose.pose.position
        orientation = msg.pose.pose.orientation

        distance = math.hypot((goal_position[0]-position.x),(goal_position[1]-position.y))

        theta = math.degrees(math.atan2((goal_position[0]-position.x),(goal_position[1]-position.y)))

        angle_1 = 2*(((orientation.w)*(orientation.z))+((orientation.x)*(orientation.y)))
        angle_2 = 1-(2*(((orientation.y)**2)+((orientation.z)**2)))

        orientation_r = math.degrees(math.atan2(angle_1,angle_2))
        print(orientation_r)

        theta_diff = theta-orientation_r
        print(theta_diff)

        if theta_diff > 0.1:
            vel_msg.angular.z = angular_vel
            self.vel_pub.publish(vel_msg)
        else:
            if distance > 0.1:
                vel_msg.angular.z = 0.0
                vel_msg.linear.x = 0.15
                self.vel_pub.publish(vel_msg)
                print(distance)
            else:
                vel_msg.angular.z = 0.0
                vel_msg.linear.x = 0.0
                self.vel_pub.publish(vel_msg)

                

def main():
    rclpy.init()
    go_goal = Navigation()
    rclpy.spin(go_goal)
    go_goal.destroy_node()
    rclpy.shutdown()
    

