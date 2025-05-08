#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node, PushRosNamespace

from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    # Launch arguments
    namespace_arg = DeclareLaunchArgument(
        'namespace',
        default_value='',
        description='Namespace for the robot'
    )
    x_pose_arg = DeclareLaunchArgument(
        'x_pose',
        default_value='0.0',
        description='X position of the robot'
    )
    y_pose_arg = DeclareLaunchArgument(
        'y_pose',
        default_value='0.0',
        description='Y position of the robot'
    )

    namespace = LaunchConfiguration('namespace')
    x_pose = LaunchConfiguration('x_pose')
    y_pose = LaunchConfiguration('y_pose')

    urdf_path ='/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/model/model.sdf'

    with open(urdf_path, 'r') as infp:
        robot_description_content = infp.read()

    # Group under namespace
    group = GroupAction([
        PushRosNamespace(namespace),

        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description_content}]
        ),

        # Spawn the robot in Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'turtlebot3',
                '-topic', 'robot_description',
                '-x', x_pose,
                '-y', y_pose,
                '-z', '0.01'
            ],
            output='screen'
        )
    ])

    return LaunchDescription([
        namespace_arg,
        x_pose_arg,
        y_pose_arg,
        group
    ])
