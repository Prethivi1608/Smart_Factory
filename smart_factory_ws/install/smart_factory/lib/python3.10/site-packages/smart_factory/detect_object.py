import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math
from geometry_msgs.msg import Twist


class DetectObject(Node):
    def __init__(self):
        super().__init__('detect_object')

        self.scan_topic = '/robot_1/robot_1/scan'
        self.velocity_pub_topic = '/robot_1/cmd_vel'
        self.detect_sub = self.create_subscription(LaserScan,self.scan_topic,self.scan_callback,10)
        self.object_distance = {}
        self.velocity_pub = self.create_publisher(Twist,self.velocity_pub_topic,10)
        self.left_angle = 345
        self.right_angle = 25
        self.angular_velocity = 0.5

    def scan_callback(self,msg):
        vel_msg = Twist()
        for i in range(len(msg.ranges)):
            if msg.ranges[i] < 1.26:
                if i<self.left_angle and i>self.right_angle:
                    vel_msg.linear.x = 0.5
                    vel_msg.angular.z = 0.0
                    self.velocity_pub.publish(vel_msg)
                else:
                    vel_msg.linear.x = 0.2
                    vel_msg.angular.z = -self.angular_velocity
                    self.velocity_pub.publish(vel_msg)


def main():
    rclpy.init()
    detect_object = DetectObject()
    rclpy.spin(detect_object)
    detect_object.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()