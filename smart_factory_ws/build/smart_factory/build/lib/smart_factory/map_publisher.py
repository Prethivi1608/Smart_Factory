import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import Header
from geometry_msgs.msg import Pose, Point, Quaternion

import yaml
import numpy as np
import cv2
import os


class MapPublisher(Node):
    def __init__(self, yaml_path):
        super().__init__('map_publisher')

        self.publisher_ = self.create_publisher(OccupancyGrid, 'map', 10)
        self.timer = self.create_timer(1.0, self.publish_map)

        self.map_msg = self.load_map(yaml_path)

    def load_map(self, yaml_path):
        with open(yaml_path, 'r') as file:
            map_metadata = yaml.safe_load(file)

        image_path = os.path.join(os.path.dirname(yaml_path), map_metadata['image'])
        resolution = float(map_metadata['resolution'])
        origin = map_metadata['origin']

        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.flip(img, 0)  # Flip vertically to match ROS coords

        height, width = img.shape
        data = []

        for i in range(height):
            for j in range(width):
                pixel = img[i][j]
                if pixel < 128:
                    data.append(100)  # occupied
                elif pixel > 250:
                    data.append(0)    # free
                else:
                    data.append(-1)   # unknown

        grid = OccupancyGrid()
        grid.header = Header()
        grid.header.frame_id = 'map'
        grid.info.resolution = resolution
        grid.info.width = width
        grid.info.height = height
        grid.info.origin = Pose(
            position=Point(x=origin[0], y=origin[1], z=0.0),
            orientation=Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)
        )
        grid.data = data
        return grid

    def publish_map(self):
        self.map_msg.header.stamp = self.get_clock().now().to_msg()
        self.publisher_.publish(self.map_msg)
        self.get_logger().info('Published map')


def main(args=None):
    rclpy.init(args=args)
    yaml_file_path = '/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/turtlebot3_housemap.yaml'
    node = MapPublisher(yaml_file_path)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()