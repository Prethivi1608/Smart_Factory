#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator

class MultiRobotNavigation(Node):
    def __init__(self):
        super().__init__('multi_robot_navigation')
        self.robot1 = BasicNavigator(namespace='tb0_0')  # Robot 1 namespace
        self.robot2 = BasicNavigator(namespace='tb0_1')  # Robot 2 namespace

    def send_goals(self, goal1, goal2):
        self.robot1.waitUntilNav2Active()
        self.robot2.waitUntilNav2Active()

        goal_pose1 = self.create_pose(goal1[0], goal1[1])
        goal_pose2 = self.create_pose(goal2[0], goal2[1])

        self.robot1.goToPose(goal_pose1)
        self.robot2.goToPose(goal_pose2)

        while not (self.robot1.isTaskComplete() and self.robot2.isTaskComplete()):
            rclpy.spin_once(self)

        self.get_logger().info('Both robots have finished navigation!')

    def create_pose(self, x, y):
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.robot1.get_clock().now().to_msg()
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.orientation.w = 1.0
        return pose

def main(args=None):
    rclpy.init(args=args)
    node = MultiRobotNavigation()
    node.send_goals((1.0, 2.0), (3.0, 1.0))  # Goal for Robot1 and Robot2
    rclpy.shutdown()

if __name__ == '__main__':
    main()
