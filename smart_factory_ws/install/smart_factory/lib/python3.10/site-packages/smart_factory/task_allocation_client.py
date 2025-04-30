import rclpy
from rclpy.node import Node
from smart_factory.srv import TaskAllocation

class TaskAllocatorClient(Node):
    def __init__(self):
        super().__init__('task_allocator_client')

        self.task_client = self.create_client(TaskAllocation,'allocate_task')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')

    def send_request(self, robot_number: int, object_name: str):
        request = TaskAllocation.Request()
        request.robot_number = robot_number
        request.object_name = object_name

        future = self.task_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            self.get_logger().info(f"Response: {future.result().message}")
        else:
            self.get_logger().error('Service call failed.')


def main(args=None):
    rclpy.init(args=args)
    task_allocator = TaskAllocatorClient()

    try:
        robot_number = 1
        object_name = 'redpringles'
        task_allocator.get_logger().info(f'Sending command: robot_number={robot_number}, object_name={object_name}')
        task_allocator.send_request(robot_number, object_name)
    finally:
        task_allocator.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()