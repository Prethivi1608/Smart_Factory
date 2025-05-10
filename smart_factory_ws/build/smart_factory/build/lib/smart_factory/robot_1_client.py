import rclpy
from rclpy.node import Node
from smart_factory_services.srv import TaskAllocation
from smart_factory import move_to_object
from smart_factory.go_to_goal import Navigation
import time

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
        self.get_logger().info(f"Requesting a goal for Robot_{robot_number}...")

        if self.future.result() is not None:
            available_goals = self.future.result().available_goals
            self.get_logger().info(f'Available goals for robot_{robot_number}:{available_goals}')
            if available_goals == 0:
                self.get_logger().info('No Goals at the moment. Waiting for goals...')
                time.sleep(1)
                self.send_request(robot_number)
            else:
                
                goal_point = self.future.result().goal_points
                self.get_logger().info(f"Response: {self.future.result().message}")
                self.get_logger().info(f"Robot_{robot_number} is now moving to {goal_point[0],goal_point[1]}....")
                
                start_time = time.time()
                duration = 15
                go_goal = Navigation(goal_point[0],goal_point[1])

                while time.time() - start_time < duration:
                    rclpy.spin_once(go_goal,timeout_sec=0.1)
                
                go_goal.destroy_node()
                
                print("Back to client node1")
                #move_to_object.main(robot_number,object_name)
                self.get_logger().info(f"Robot_{robot_number} reached {goal_point}")
                self.send_request(robot_number)

                go_goal.destroy_node()
        else:
            self.get_logger().error('Service call failed.')
def main():
    rclpy.init()
    robot_number = 1
    task_allocator = TaskAllocatorClient()
    task_allocator.get_logger().info(f'Getting goals for robot_{robot_number}')
    task_allocator.send_request(robot_number)
    task_allocator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()