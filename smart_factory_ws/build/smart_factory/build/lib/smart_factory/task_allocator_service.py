import rclpy
from rclpy.node import Node
from smart_factory.srv import TaskAllocation

class TaskAllocatorService(Node):
    def __init__(self):
        super().__init__('task_allocator_service')

        self.task_service = self.create_service(TaskAllocation,'allocate_task',self.allocate_callback)

    def allocate_callback(self,request,response):
        number = request.robot_number
        name = request.object_name

        if number and name is not None:
            response.success = True
            response.message = f'Robot{number} is moving to {name}'
        else:
            response.success = False
            response.message = 'No message recieved'

def main():
    rclpy.init()
    task_allocator = TaskAllocatorService()
    rclpy.spin(task_allocator)
    task_allocator.destroy_node()
    rclpy.shutdown()


