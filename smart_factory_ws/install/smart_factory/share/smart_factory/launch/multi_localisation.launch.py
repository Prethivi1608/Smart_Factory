from launch_ros.actions import Node
from launch import LaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    nav2_yaml_1 = os.path.join(get_package_share_directory('smart_factory'),'config','robot1_nav2_params.yaml')
    nav2_yaml_2 = os.path.join(get_package_share_directory('smart_factory'),'config','robot2_nav2_params.yaml')
    
    package_dir = get_package_share_directory('smart_factory')
    
    map_file = '/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/maps/turtlebot3_housemap.yaml'

    map_server = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{'use_sim_time':True},
                    {'topic_name':'map'},
                    {'frame_name':'map'},
                    {'yaml_filename': map_file}]
    )

    amcl_robot1 = Node(
        namespace='robot_1',
        package='nav2_amcl',
        executable='amcl',
        name='amcl',
        output='screen',
        parameters=[nav2_yaml_1]
        
    )

    amcl_robot2 = Node(
        namespace='robot_2',
        package='nav2_amcl',
        executable='amcl',
        name='amcl',
        output='screen',
        parameters=[nav2_yaml_2]
        
    )

    nav2_lifecycle = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_local',
        output='screen',
        parameters=[{'use_sim_time':True},
                    {'autostart':True},
                    {'node_names':['map_server','robot_1/amcl','robot_2/amcl_2']}]
        
    )

    
    ld = LaunchDescription()
    ld.add_action(map_server)
    ld.add_action(amcl_robot1)
    ld.add_action(amcl_robot2)
    ld.add_action(nav2_lifecycle)

    return ld

