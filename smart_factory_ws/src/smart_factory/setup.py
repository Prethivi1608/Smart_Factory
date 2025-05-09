from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'smart_factory'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),glob('launch/*')),
        (os.path.join('share',package_name,'model'),glob('model/*')),
        (os.path.join('share',package_name,'world'),glob('world/*')),
        (os.path.join('share',package_name,'config'),glob('config/*')),
        (os.path.join('share',package_name,'yolo_model'),glob('yolo_model/*')),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='prethiviraj',
    maintainer_email='prethiviraj@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'path_planning = smart_factory.path_planning:main',
            'example_client= smart_factory.map_publisher:main',
            'example_service= smart_factory.get_position:main',
            'camera_publisher= smart_factory.camera_publisher:main',
            'camera_classifier= smart_factory.camera_classifier:main',
            'camera_object= smart_factory.camera_object:main',
            'move_to_object= smart_factory.move_to_object:main',
            'go_to_goal= smart_factory.go_to_goal:main',
            'camera_info= smart_factory.camera_info:main',
            'camera_distance= smart_factory.camera_distance:main',
            'image_capture= smart_factory.image_capture:main',
            'nav_to_pose= smart_factory.nav_to_pose:main',
            'nav_thro_pose= smart_factory.nav_thro_pose:main',
            'detect_object= smart_factory.detect_object:main',
            'goals_assigner = smart_factory.goals_assigner:main',
            'robot_1_client = smart_factory.robot_1_client:main',
            'robot_2_client = smart_factory.robot_2_client:main',
            
        ],

    },
)
