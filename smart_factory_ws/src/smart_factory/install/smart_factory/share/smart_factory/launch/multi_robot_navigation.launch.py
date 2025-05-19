from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    namespace = 'robot_1'

    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    nav2_launch_file = os.path.join(nav2_bringup_dir, 'launch', 'bringup_launch.py')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(nav2_launch_file),
            launch_arguments={
                'namespace': namespace,
                'use_namespace': 'true',
                'autostart': 'true',
                'map': '/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/maps/turtlebot3_housemap.yaml',
                'params_file': '/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/config/robot1_nav2_params.yaml',
                'use_sim_time': 'true'  # if using simulation
            }.items()
        )
    ])

