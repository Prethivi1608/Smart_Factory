import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    TURTLEBOT3_MODEL = 'waffle'

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    urdf_file_name = 'tb3_' + TURTLEBOT3_MODEL + '.urdf'

    print('urdf_file_name : {}'.format(urdf_file_name))

    urdf_path = os.path.join(
        get_package_share_directory('smart_factory'),
        'model',
        urdf_file_name)

    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'use_sim_time': use_sim_time,
                'robot_description': robot_desc
            }],
        ),
    ])