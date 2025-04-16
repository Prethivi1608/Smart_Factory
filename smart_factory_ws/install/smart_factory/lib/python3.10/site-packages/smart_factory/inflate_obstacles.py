import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
import numpy as np
import cv2



class InflationNode(Node):
    def __init__(self):
        super().__init__('inflation_node')

        self.subscription = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            10)

        self.publisher_ = self.create_publisher(
            OccupancyGrid,
            '/inflated_map',
            10)

        # Parameters (can be dynamically reconfigured later)
        self.robot_radius = 0.2  # meters
        self.inflation_radius = 0.1  # meters

    def map_callback(self, msg):
        resolution = msg.info.resolution
        width = msg.info.width
        height = msg.info.height

        # Convert to numpy array
        grid = np.array(msg.data, dtype=np.int8).reshape((height, width))

        # Apply inflation
        inflated_grid = self.inflate_with_distance_transform(grid, self.robot_radius + self.inflation_radius, resolution)

        # Convert back to OccupancyGrid
        new_msg = OccupancyGrid()
        new_msg.header = msg.header
        new_msg.info = msg.info
        new_msg.data = inflated_grid.flatten().tolist()

        self.publisher_.publish(new_msg)

    def inflate_with_distance_transform(self, grid, inflation_radius, resolution):
        # Convert to OpenCV format
        obstacle_mask = (grid == 100).astype(np.uint8)

        # Invert for distance transform
        inverted = cv2.bitwise_not(obstacle_mask * 255)

        # Distance transform
        dist_transform = cv2.distanceTransform(inverted, cv2.DIST_L2, 5)

        # Convert inflation radius to pixels
        inflation_pixels = int(inflation_radius / resolution)

        # Apply inflation
        inflated = (dist_transform <= inflation_pixels).astype(np.uint8) * 100

        inflated_grid = np.maximum(grid, inflated).astype(np.int8)
        return inflated_grid


def main(args=None):
    rclpy.init(args=args)
    node = InflationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
