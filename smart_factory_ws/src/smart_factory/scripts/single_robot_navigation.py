#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult

class SingleRobotNavigation(Node):
    def __init__(self):
        super().__init__('single_robot_navigation')
        self.navigator = BasicNavigator()

    def send_goal(self, x, y):
        self.navigator.waitUntilNav2Active()

        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = self.navigator.get_clock().now().to_msg()
        goal_pose.pose.position.x = x
        goal_pose.pose.position.y = y
        goal_pose.pose.orientation.w = 1.0

        self.navigator.goToPose(goal_pose)

        while not self.navigator.isTaskComplete():
            rclpy.spin_once(self)

        result = self.navigator.getResult()

        if result == TaskResult.SUCCEEDED:
            self.get_logger().info('Goal reached successfully.')
        else:
            self.get_logger().info('Goal failed or canceled.')

def main(args=None):
    rclpy.init(args=args)
    node = SingleRobotNavigation()
    node.send_goal(2.0, 3.0)  # Example goal coordinates
    rclpy.shutdown()

if __name__ == '__main__':
    main()
