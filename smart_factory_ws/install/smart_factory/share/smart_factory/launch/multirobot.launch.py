#!/usr/bin/env python3
#
# Copyright 2019 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: Joep Tool, HyunGyu Kim

import os
import xml.etree.ElementTree as ET

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import GroupAction
from launch.actions import IncludeLaunchDescription
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnShutdown
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import PushRosNamespace
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node


def generate_launch_description():

    number_of_robots = 2
    namespace = 'robot'
    pose = [[-2, -0.5],[-0.5, 2]]
    urdf_path = os.path.join(
        get_package_share_directory('smart_factory'),
        'model',
        'model.sdf'
    )
    save_path = os.path.join(
        get_package_share_directory('smart_factory'),
        'model',
        'tmp'
    )
    launch_file_dir = os.path.join(get_package_share_directory('smart_factory'), 'launch')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    world = os.path.join(
        get_package_share_directory('smart_factory'),
        'world',
        'turtlebot3_house.world'
    )

    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world}.items()
    )

    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        )
    )

    robot_state_publisher_cmd_list = []

    for count in range(number_of_robots):
        robot_state_publisher_cmd_list.append(
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(launch_file_dir, 'robot_state_publisher.launch.py')
                ),
                launch_arguments={
                    'use_sim_time': use_sim_time,
                    'frame_prefix': f'{namespace}{count+1}'
                    }.items()
            )
        )
    
    slam_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource([
        PathJoinSubstitution([FindPackageShare('smart_factory'),'launch','online_async_launch.py'])]),
        launch_arguments={
            
            'slam_params_file':PathJoinSubstitution([FindPackageShare('smart_factory'),'config','mapper_params_online_async.yaml']),'use_sim_time':'true'}.items()
        
        )

    spawn_turtlebot_cmd_list = []

    for count in range(number_of_robots):
        tree = ET.parse(urdf_path)
        root = tree.getroot()
        for odom_frame_tag in root.iter('odometry_frame'):
            odom_frame_tag.text = f'{namespace}{count+1}/odom'
        for base_frame_tag in root.iter('robot_base_frame'):
            base_frame_tag.text = f'{namespace}{count+1}/base_footprint'
        for scan_frame_tag in root.iter('frame_name'):
            scan_frame_tag.text = f'{namespace}{count+1}/base_scan'
        urdf_modified = ET.tostring(tree.getroot(), encoding='unicode')
        urdf_modified = '<?xml version="1.0" ?>\n'+urdf_modified
        with open(f'{save_path}{count+1}.sdf', 'w') as file:
            file.write(urdf_modified)

        spawn_turtlebot_cmd_list.append(
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(launch_file_dir, 'multi_spawn_turtlebot3.launch.py')
                ),
                launch_arguments={
                        'x_pose': str(pose[count][0]),
                        'y_pose': str(pose[count][1]),
                        'robot_name': f' tb3_{count+1}',
                        'namespace': f'{namespace}{count+1}',
                        'sdf_path': f'{save_path}{count+1}.sdf'
                }.items()
            )
        )
    
    
    rviz_Node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d',PathJoinSubstitution([
            FindPackageShare('smart_factory'), 'config', 'slam_config.rviz'
        ])]
        )

    ld = LaunchDescription()
    # Add the commands to the launch description
    #ld.add_action(rviz_Node)
    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)
    ld.add_action(RegisterEventHandler(
        OnShutdown(
            on_shutdown=lambda event,
            context: [os.remove(f'{save_path}{count+1}.sdf') for count in range(number_of_robots)]
        )
    ))
    for count, spawn_turtlebot_cmd in enumerate(spawn_turtlebot_cmd_list, start=1):
        ld.add_action(GroupAction([PushRosNamespace(f'{namespace}{count}'),
                                  robot_state_publisher_cmd_list[count-1],
                                  spawn_turtlebot_cmd]))
    
    #ld.add_action(slam_launch)

    return ld