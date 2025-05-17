from smart_factory_services.srv import RobotStatus
import rclpy
from rclpy.node import Node



class RobotStatus(Node):
    def __init__(self):
        super().__init__('robot_status_service')

        self.create_service(RobotStatus,'robot_status',self.status_callback)

        self.robot = self.robot = '/' + 'robot_' + str(self.number)

        self.create_subscription()
    
    def status_callback(self,request,response):
        self.number = request.robot_number




