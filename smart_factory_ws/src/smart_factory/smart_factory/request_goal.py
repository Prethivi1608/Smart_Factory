import rclpy
from rclpy.node import Node
from smart_factory_services.srv import TaskAllocation
from smart_factory.move_to_object import MovetoObject
from smart_factory.go_to_goal import Navigation
import time

class RequestGoal(Node):
    def __init__(self,robot):
        super().__init__(f'{robot}_request')

        self.task_client = self.create_client(TaskAllocation,'allocate_task')
        self.robot = robot
        self.pick_goal = None
        self.object_goal = None
        self.drop_goal = None

        self.status = None

        while not self.task_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')
    
    def send_request(self, robot_number: int):
        request = TaskAllocation.Request()
        request.robot_number = robot_number

        self.future = self.task_client.call_async(request)
        rclpy.spin_until_future_complete(self, self.future)
        self.get_logger().info(f"Requesting a goal for Robot_{robot_number}...")

        if self.future.result() is not None:
            available_goals = self.future.result().available_goals
            self.get_logger().info(f'Available goals for robot_{robot_number}:{available_goals}')
            if available_goals == 0:
                self.get_logger().info('No Goals at the moment. Waiting for goals...')
                self.status = 'No goals at the moment'
            else:
                self.pick_goal = self.future.result().pick_goal
                self.object_goal = self.future.result().object_goal
                self.drop_goal = self.future.result().drop_goal
                self.status = 'Goals Assigned'

        else:
            self.get_logger().error('Service call failed.')
            self.status = 'Service not found'
    

        return self.status

    


# def main():
#     rclpy.init()
#     robot_number = 1
#     robot = f'robot_'+ str(robot_number)
#     task_allocator = RequestGoal(robot)
#     task_allocator.get_logger().info(f'Getting goals for robot_{robot_number}')
#     task_allocator.send_request(robot_number)
#     task_allocator.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()