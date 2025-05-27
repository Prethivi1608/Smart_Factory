import rclpy
from rclpy.node import Node
from smart_factory_services.srv import TaskAllocation
from smart_factory.move_to_object import MovetoObject
from smart_factory.go_to_goal import Navigation
import time

class TaskAllocatorClient(Node):
    def __init__(self,robot):
        super().__init__('robot_1_client')

        self.task_client = self.create_client(TaskAllocation,'allocate_task')
        self.robot = robot

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
                
                pick_goal = self.future.result().pick_goal
                object_goal = self.future.result().object_goal
                drop_goal = self.future.result().drop_goal
                self.get_logger().info(f"Response: {self.future.result().message}")
                self.get_logger().info(f"Robot_{robot_number} is now moving to {pick_goal[0],pick_goal[1]} to pick up {object_goal} and dropping at {drop_goal[0],drop_goal[1]}")
                
                #self.go_to_goal(pick_goal[0],pick_goal[1],self.robot,robot_number)
                self.get_logger().info(f"Robot_{robot_number} reached {pick_goal[0]},{pick_goal[1]}")

                #self.move_to_object(robot_number,object_goal)
                self.get_logger().info(f'Robot has picked {object_goal}')
                time.sleep(5)


                self.get_logger().info(f'Robot moving to drop location: {drop_goal[0]},{drop_goal[1]}')
                #self.go_to_goal(drop_goal[0],drop_goal[1],self.robot,robot_number)
                self.get_logger().info(f"Robot_{robot_number} reached {drop_goal[0]},{drop_goal[1]}. Waiting for the {object_goal} to be dropped...")
                


                self.send_request(robot_number)

        else:
            self.get_logger().error('Service call failed.')


    
    def go_to_goal(self,goal_x,goal_y,robot,robot_number):
        start_time = time.time()
        duration = 20
        go_goal = Navigation(goal_x,goal_y,robot,robot_number)

        while time.time() - start_time < duration:
            rclpy.spin_once(go_goal,timeout_sec=0.1)
        
        go_goal.destroy_node()

    def move_to_object(self,robot_number,object_name):
        
        start_time = time.time()

        duration = 50
        move_to_object = MovetoObject(robot_number,object_name)

        while time.time() - start_time < duration:
            rclpy.spin_once(move_to_object,timeout_sec=0.1)
        
        move_to_object.destroy_node()





def main():
    rclpy.init()
    robot_number = 1
    robot = f'robot_'+ str(robot_number)
    task_allocator = TaskAllocatorClient(robot)
    task_allocator.get_logger().info(f'Getting goals for robot_{robot_number}')
    task_allocator.send_request(robot_number)
    task_allocator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()