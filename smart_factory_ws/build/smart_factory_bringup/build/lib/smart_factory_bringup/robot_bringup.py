import subprocess
import rclpy
from rclpy.node import Node
from smart_factory_services.srv import TaskAllocation
# from smart_factory_services.srv import RobotStatus

from std_msgs.msg import String

class Robot(Node):
    def __init__(self,number,robot_id):
        super().__init__(f'robot_{robot_id}')

        self.robot_number = number # Number on the namespace
        self.robot_id = robot_id # Id of the turtlebot. Number on the top.
        self.robot_name = 'robot' 

    def robot_startup(self):
        
        pass
        
        # subprocess.run(robot_bringup_command)


        






def main():
    rclpy.init()
    robot_id = input('Enter the Robot ID: \n')
    robot_number = input(f'Enter the number of Robot-{robot_id} \n')

    robot = Robot(robot_number,robot_id)
    rclpy.spin(robot)
    robot.destroy_node()
    rclpy.shutdown()

    
        
        