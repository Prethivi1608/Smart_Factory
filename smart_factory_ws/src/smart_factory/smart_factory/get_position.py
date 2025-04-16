import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
import math


class GetPosition(Node):
    def __init__(self):
        super().__init__('get_position_')
        
        self.pos_topic = '/odom'
        self.scan_topic = '/scan'
        
        self.position_sub = self.create_subscription(Odometry,self.pos_topic,self.odom_callback,10)
        #self.laser_sub = self.create_subscription(LaserScan,self.scan_topic,self.scan_callback,10)
        
    def odom_callback(self,msg):
        position = msg.pose.pose.position
        orientation = msg.pose.pose.orientation      
        
        self.get_logger().info(f'Robot Position: x:{position.x},y:{position.y},z:{position.z},w={orientation.w}')
        
    def scan_callback(self,msg):
        angle_min = msg.angle_min
        angle_max = msg.angle_max
        ranges = msg.ranges
        for i,j in enumerate(ranges):
            if j < 2:
                print(f'angle:{i},distance:{j}')
        
        self.get_logger().info(f'angle_min: {angle_min},angle_max: {angle_max},ranges: {ranges}')
        

def main():
    rclpy.init()
    get_pos = GetPosition()
    rclpy.spin(get_pos)
    get_pos.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()        
        