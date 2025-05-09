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

    
    slam_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource([
        PathJoinSubstitution([FindPackageShare('smart_factory'),'launch','online_async_launch.py'])]),
        launch_arguments={
            
            'slam_params_file':PathJoinSubstitution([FindPackageShare('smart_factory'),'config','mapper_params_online_async.yaml']),'use_sim_time':'true'}.items()
        
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
    ld.add_action(rviz_Node)
    
    ld.add_action(slam_launch)

    return ld