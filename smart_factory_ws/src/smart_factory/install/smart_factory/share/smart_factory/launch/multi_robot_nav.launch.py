#!/usr/bin/env python3
 
import os
import xml.etree.ElementTree as ET
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, GroupAction, RegisterEventHandler
from launch.event_handlers import OnShutdown
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import PushRosNamespace, Node
 
def generate_launch_description():
    number_of_robots = 2
    robot_namespaces = ['tb3_1', 'tb3_2']
    poses = [[2.0, 2.0], [4.0, 2.0]]
 
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
 
    autonomous_tb3_dir = get_package_share_directory('autonomous_tb3')
    smart_factory_dir = get_package_share_directory('smart_factory')
    nav2_dir = get_package_share_directory('nav2_bringup')
    gazebo_ros_dir = get_package_share_directory('gazebo_ros')
 
    map_file = os.path.join(autonomous_tb3_dir, 'config', 'maze.yaml')
    nav_params_file = os.path.join(autonomous_tb3_dir, 'config', 'tb3_nav_params.yaml')
    rviz_config_file = os.path.join(autonomous_tb3_dir, 'config', 'tb3_nav.rviz')
    sdf_model = os.path.join(smart_factory_dir, 'model', 'model.sdf')
    sdf_tmp_dir = os.path.join(smart_factory_dir, 'model', 'tmp')
    os.makedirs(sdf_tmp_dir, exist_ok=True)
 
    world_file = os.path.join(autonomous_tb3_dir, 'world', 'maze', 'maze.world')
 
    # Gazebo server and client
    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(gazebo_ros_dir, 'launch', 'gzserver.launch.py')),
        launch_arguments={'world': world_file}.items()
    )
    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(gazebo_ros_dir, 'launch', 'gzclient.launch.py'))
    )
 
    # RViz
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file],
        parameters=[{'use_sim_time': True}]
    )
 
    # Clean up SDF files on shutdown
    shutdown_cleanup = RegisterEventHandler(
        OnShutdown(on_shutdown=lambda event, context: [
            os.remove(os.path.join(sdf_tmp_dir, f'{i+1}.sdf')) for i in range(number_of_robots)
        ])
    )
 
    group_launches = []
 
    for i in range(number_of_robots):
        ns = robot_namespaces[i]
        x_pose, y_pose = poses[i]
 
        # Modify SDF model with correct TF prefixes
        tree = ET.parse(sdf_model)
        root = tree.getroot()
        for odom in root.iter('odometry_frame'):
            odom.text = f'{ns}/odom'
        for base in root.iter('robot_base_frame'):
            base.text = f'{ns}/base_footprint'
        for scan in root.iter('frame_name'):
            scan.text = f'{ns}/base_scan'
        urdf_mod = ET.tostring(root, encoding='unicode')
        urdf_mod = '<?xml version="1.0" ?>\n' + urdf_mod
        modified_path = os.path.join(sdf_tmp_dir, f'{i+1}.sdf')
        with open(modified_path, 'w') as f:
            f.write(urdf_mod)
 
        # robot_state_publisher
        state_pub = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(smart_factory_dir, 'launch', 'robot_state_publisher.launch.py')),
            launch_arguments={'use_sim_time': 'true', 'frame_prefix': ns}.items()
        )
 
        # spawn robot
        spawn = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(smart_factory_dir, 'launch', 'multi_spawn_turtlebot3.launch.py')),
            launch_arguments={
                'x_pose': str(x_pose),
                'y_pose': str(y_pose),
                'robot_name': ns,
                'namespace': ns,
                'sdf_path': modified_path
            }.items()
        )
 
        # nav2 bringup per robot
        nav2 = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(nav2_dir, 'launch', 'bringup_launch.py')),
            launch_arguments={
                'namespace': ns,
                'map': map_file,
                'use_sim_time': 'true',
                'params_file': nav_params_file
            }.items()
        )
 
        group = GroupAction([
            PushRosNamespace(ns),
            state_pub,
            spawn,
            nav2
        ])
        group_launches.append(group)
 
    ld = LaunchDescription()
    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)
    ld.add_action(rviz_node)
    ld.add_action(shutdown_cleanup)
 
    for group in group_launches:
        ld.add_action(group)
 
    return ld