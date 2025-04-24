from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
import os
from ament_index_python import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():


    config_dir = os.path.join(get_package_share_directory('smart_factory'),'config')
    
    go_to_object_robot1 = Node(
        package='smart_factory',
        executable= 'move_to_object',
        name='move_to_object',
        output='screen',
        parameters=[
            os.path.join(config_dir,'move_to_object.yaml'),
            {'robot_number': 1,
            'object_name' : 'greenpringles'
        }]
    )

    go_to_object_robot2 = Node(
        package='smart_factory',
        executable= 'move_to_object',
        name='move_to_object',
        output='screen',
        parameters=[
            os.path.join(config_dir,'move_to_object.yaml'),
            {'robot_number': 2,
            'object_name' : 'redpringles'
        }]
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )
    

    ld = LaunchDescription()

    ld.add_action(go_to_object_robot1)
    ld.add_action(go_to_object_robot2)
    ld.add_action(rviz_node)

    return ld