from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
import os
from ament_index_python import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    robot_1 = Node(
        package='smart_factory',
        executable= 'robot_1_client',
        name='robot_1',
        output='screen'
    )

    robot_2 = Node(
        package='smart_factory',
        executable= 'robot_2_client',
        name='robot_2',
        output='screen'
    )
    
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )
    

    ld = LaunchDescription()

    ld.add_action(robot_1)
    ld.add_action(robot_2)
    # ld.add_action(rviz_node)

    return ld