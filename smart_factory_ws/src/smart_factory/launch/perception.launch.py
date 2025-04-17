from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():


    camera_pub_node = Node(
        package= 'smart_factory',
        executable= 'camera_publisher',
        name= 'camera_pub',
        output= 'screen'
    )

    camera_classify_node = Node(
        package='smart_factory',
        executable= 'camera_classifier',
        name='camera_class',
        output='screen'
    )

    camera_distance_node = Node(
        package='smart_factory',
        executable= 'camera_distance',
        name='camera_dist',
        output='screen'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    ld = LaunchDescription()

    #ld.add_action(camera_pub_node)
    ld.add_action(camera_classify_node)
    ld.add_action(camera_distance_node)
    ld.add_action(rviz_node)

    return ld