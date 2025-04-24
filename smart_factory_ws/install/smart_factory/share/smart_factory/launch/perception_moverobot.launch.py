from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
import os
from ament_index_python import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    
    camera_classify_node = Node(
        package='smart_factory',
        executable= 'camera_class_gz',
        name='camera_class',
        output='screen'
    )


    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )
    

    ld = LaunchDescription()

    ld.add_action(camera_classify_node)
    ld.add_action(rviz_node)

    return ld