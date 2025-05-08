import rclpy
from rclpy.node import Node
from smart_factory_services.srv import TaskAllocation
import random
from smart_factory import move_to_object

class TaskAllocatorClient(Node):
    def __init__(self):
        super().__init__('task_allocator_client')

        self.task_client = self.create_client(TaskAllocation,'allocate_task')

        while not self.task_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')

    def send_request(self, robot_number: int):
        request = TaskAllocation.Request()
        request.robot_number = robot_number

        self.future = self.task_client.call_async(request)
        rclpy.spin_until_future_complete(self, self.future)

        if self.future.result() is not None:
            self.get_logger().info(f"Response: {self.future.result().message}")
            #object_name = self.future.result().object_name
            #move_to_object.main(robot_number,object_name)
        else:
            self.get_logger().error('Service call failed.')
def main():
    rclpy.init()
    robot_number = input("Choose the available robot:\n1. robot_1\n2. robot_2\n")
    if robot_number == '1':
        robot_number = 1
    else: robot_number = 2
    task_allocator = TaskAllocatorClient()
    task_allocator.get_logger().info(f'Getting goals for robot_{robot_number}')
    task_allocator.send_request(robot_number)
    task_allocator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()