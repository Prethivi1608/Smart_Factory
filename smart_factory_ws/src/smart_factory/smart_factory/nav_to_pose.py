
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration


def main(initial_x,initial_y,initial_orient,goal_x,goal_y):
    if not rclpy.ok():
        rclpy.init()

    navigator = BasicNavigator()

    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    initial_pose.pose.position.x = initial_x
    initial_pose.pose.position.y = initial_y
    initial_pose.pose.orientation.w = initial_orient
    navigator.setInitialPose(initial_pose)

    navigator.waitUntilNav2Active()

    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose.pose.position.x = goal_x
    goal_pose.pose.position.y = goal_y
    goal_pose.pose.orientation.w = 0.707108075392169

    navigator.goToPose(goal_pose)

    i = 0
    while not navigator.isTaskComplete():

        i = i + 1
        feedback = navigator.getFeedback()
        if feedback and i % 5 == 0:
            print('Estimated time of arrival: ' + '{0:.0f}'.format(
                  Duration.from_msg(feedback.estimated_time_remaining).nanoseconds / 1e9)
                  + ' seconds.')

            if Duration.from_msg(feedback.navigation_time) > Duration(seconds=600.0):
                navigator.cancelTask()

    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        print('Goal succeeded!')
        return
    elif result == TaskResult.CANCELED:
        print('Goal was canceled!')
        return
    elif result == TaskResult.FAILED:
        print('Goal failed!')
        return
    else:
        print('Goal has an invalid return status!')
        return

    # # navigator.lifecycleShutdown()
    # rclpy.shutdown()
    # print("in nav_to_pose")
    # return