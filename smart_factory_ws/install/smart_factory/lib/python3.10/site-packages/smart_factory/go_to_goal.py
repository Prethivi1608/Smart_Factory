import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist,Point,Quaternion
import math
import time
import numpy as np
from smart_factory import nav_to_pose
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from rclpy.duration import Duration

class Navigation(Node):
    def __init__(self,goal_x,goal_y):
        super().__init__('go_to_goal')
        
        self.pos_topic = '/odom'
        self.vel_topic = '/cmd_vel'
        self.pos_sub = self.create_subscription(Odometry,self.pos_topic,self.odom_callback,10)
        self.vel_pub = self.create_publisher(Twist,self.vel_topic,10)
        # self.timer = self.create_timer(0.5, self.check_done_callback)
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.robot_position_x = None
        self.robot_position_y = None
        self.robot_orientation_w = None
        self.result = None
        self.navigator = BasicNavigator()
        self.navigator.waitUntilNav2Active()
        self.done = False

        
    def odom_callback(self,msg):

        position = msg.pose.pose.position
        orientation = msg.pose.pose.orientation
        self.robot_position_x = position.x
        self.robot_position_y = position.y
        self.robot_orientation_w = orientation.w

        if self.robot_position_x is not None and self.robot_position_y is not None:
            self.result = self.go_to_goal(self.robot_position_x,self.robot_position_y,self.robot_orientation_w,self.goal_x,self.goal_y)
            print(f'result={self.result}')
            # self.done = True
    
    
    # def check_done_callback(self):
    #     if self.done:
    #         print('shutting down the node')
    #         self.destroy_node()
    #         rclpy.shutdown()



    def go_to_goal(self,initial_x,initial_y,initial_orient,goal_x,goal_y):

        initial_pose = PoseStamped()
        initial_pose.header.frame_id = 'map'
        initial_pose.header.stamp = self.navigator.get_clock().now().to_msg()
        initial_pose.pose.position.x = initial_x
        initial_pose.pose.position.y = initial_y
        initial_pose.pose.orientation.w = initial_orient
        self.navigator.setInitialPose(initial_pose)

        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = self.navigator.get_clock().now().to_msg()
        goal_pose.pose.position.x = goal_x
        goal_pose.pose.position.y = goal_y
        goal_pose.pose.orientation.w = 0.707108075392169

        self.navigator.goToPose(goal_pose)

        i = 0
        while not self.navigator.isTaskComplete():

            i = i + 1
            feedback = self.navigator.getFeedback()
            if feedback and i % 5 == 0:
                print('Estimated time of arrival: ' + '{0:.0f}'.format(
                    Duration.from_msg(feedback.estimated_time_remaining).nanoseconds / 1e9)
                    + ' seconds.')

                if Duration.from_msg(feedback.navigation_time) > Duration(seconds=600.0):
                    self.navigator.cancelTask()

        result = self.navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            print('Goal succeeded!')
            return result
        elif result == TaskResult.CANCELED:
            print('Goal was canceled!')
            return result
        elif result == TaskResult.FAILED:
            print('Goal failed!')
            return result
        else:
            print('Goal has an invalid return status!')
            return result
        

# def main(goal_x,goal_y):
#     if not rclpy.ok():
#         rclpy.init()
#     go_goal = Navigation(goal_x,goal_y)
#     rclpy.spin_once(go_goal, timeout_sec=120.0)
#     go_goal.destroy_node()
#     rclpy.shutdown()
#     print("Exiting main function...")
#     #return


# if __name__ == '__main__':
#     main()

