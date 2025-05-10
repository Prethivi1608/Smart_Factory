from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

import os

def generate_launch_description():
    namespace = LaunchConfiguration('namespace', default='robot_1')
    map_file = '/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/turtlebot3_housemap.yaml'
    params_file = PathJoinSubstitution([FindPackageShare('smart_factory'),'config','nav2_params.yaml'])
    rviz_config_file = PathJoinSubstitution([FindPackageShare('smart_factory'),'config','nav2_default_view.rviz'])

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('nav2_bringup'),
                '/launch/bringup_launch.py'
            ]),
            launch_arguments={
                'namespace': namespace,
                'use_namespace': 'true',
                'map': map_file,
                'autostart': 'true',
                'params_file': params_file 
            }.items()
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            namespace=namespace,
            arguments=['-d', rviz_config_file],
            output='screen'
        )
    ])
