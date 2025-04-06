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
            'robot_move = smart_factory.robot_move:main',
            'get_position = smart_factory.get_position:main',
            'go_to_goal = smart_factory.go_to_goal:main',
            
        ],
    },
)
