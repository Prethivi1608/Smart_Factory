# This file goes into the turtlebot. Copy yhis launch file into the turtlebot
# It contains both the bringup file and camera node. This starts up the turtlebot. - Robot number and camera_format are dynmaically adjusted through the python script

from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    
    
    robot_number_arg = DeclareLaunchArgument(
        'robot_number',
        default_value='1',
        description='Namespace of the robot'
    )

    camera_type_arg = DeclareLaunchArgument(
        'camera_format',
        default_value= 'RGB888',
        description= 'Type of the camera' 
    )
    
    robot_number = LaunchConfiguration('robot_number') # Give the robot_number in the python script - smart_factory_bringup --> robot_bringup.py
    
    camera_format_type = LaunchConfiguration('camera_format') # Give the robot_number in the python script - smart_factory_bringup --> robot_bringup.py
    
    camera_topic = '/camera/image_raw'
    robot = f'robot_'+str(robot_number)
    robot_camera_topic = robot+camera_topic
    

    robot_bringup_node = Node(
        package= 'multi_robot_bringup', 
        executable= 'namespaced_robot.launch.py',
        name= 'robot_bringup_node',
        namespace= robot
    ) # bringup the robot (state publisher and differential drive controller)

    camera_node = Node(
        package= 'camera_ros',
        executable= 'camera_node',
        name= 'camera_node',
        parameters= [{ 
            'format': camera_format_type,
            'width': 160,
            'height': 120 
            }],
        
        remappings= [
            (camera_topic,robot_camera_topic) # Check if the topic concat. else, change to string
            ]
    ) # Bringup the camera_node



    return LaunchDescription([
        robot_number_arg,
        camera_type_arg,
        robot_bringup_node,
        camera_node
    ])
