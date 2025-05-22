from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'smart_factory_simulations'

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
        (os.path.join('share',package_name,'maps'),glob('maps/*')),
        (os.path.join('share',package_name,'config'),glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='prethivi',
    maintainer_email='prethiviraj@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'goals_assigner = smart_factory_simulations.goals_assigner:main',
            'move_to_object = smart_factory_simulations.move_to_object:main',
            'robot_bringup = smart_factory_simulations.robot_bringup:main',
        ],
    },
)
