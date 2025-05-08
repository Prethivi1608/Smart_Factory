import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math
from geometry_msgs.msg import Twist
import time
from std_msgs.msg import String


class DetectObject(Node):
    def __init__(self,robot_number):
        super().__init__('detect_object')

        self.robot_number = self.get_parameter('robot_number').get_parameter_value().integer_value
        self.robot = '/robot' + '_' + str(self.robot_number)
        self.scan_topic = self.robot + '/scan'
        self.velocity_pub_topic = self.robot + '/cmd_vel'
        self.status_pub_topic = self.robot + '/robot_status'
        self.detect_sub = self.create_subscription(LaserScan,self.scan_topic,self.scan_callback,10)
        self.object_distance = {}
        self.velocity_pub = self.create_publisher(Twist,self.velocity_pub_topic,10)
        self.status_publisher = self.create_publisher(String,self.status_pub_topic,10)
        
        self.left_angle = 345
        self.right_angle = 25
        self.angular_velocity = 0.5


    def scan_callback(self,msg):
        status_msg = String()
        vel_msg = Twist()
        for i in range(len(msg.ranges)):
            if msg.ranges[i] < 1.26:
                if i<self.left_angle and i>self.right_angle:
                    vel_msg.linear.x = 0.5
                    vel_msg.angular.z = 0.0
                    self.velocity_pub.publish(vel_msg)
                    self.robot_status = 'Moving'
                    status_msg.data = self.robot_status
                    self.status_publisher.publish(status_msg)
                else:
                    vel_msg.linear.x = 0.2
                    vel_msg.angular.z = -self.angular_velocity
                    self.velocity_pub.publish(vel_msg)
                    self.robot_status = 'Moving'
                    status_msg.data = self.robot_status
                    self.status_publisher.publish(status_msg)

def main():
    if not rclpy.ok():
        rclpy.init()
    # number = input('Choose the robot\n1. Robot1\n2. Robot2\n')
    # if number == '1':
    #     number = 1
    # else:
    #     number = 2
    number = 1
    detect_object = DetectObject(number)
    rclpy.spin(detect_object)
    detect_object.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()