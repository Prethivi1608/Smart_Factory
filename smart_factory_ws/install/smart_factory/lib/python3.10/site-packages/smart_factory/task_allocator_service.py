import rclpy
from rclpy.node import Node
from smart_factory_services.srv import TaskAllocation

class TaskAllocatorService(Node):
    def __init__(self,robot_goals):
        super().__init__('task_allocator_service')

        self.task_service = self.create_service(TaskAllocation,'allocate_task',self.allocate_callback)
        self.goal_name = robot_goals

    def allocate_callback(self,request,response):
        number = request.robot_number

        if number is not None:
            response.success = True
            if len(self.goal_name) == 0:
                response.message = f'No goals to assign for robot_{number}'
                self.get_logger().info('No goals to assign')
            else:
                goal_name = self.goal_name[0]
                response.object_name = goal_name
                response.message = f'{goal_name} goal is assigned to robot_{number}'
                del self.goal_name[0]
                print(self.goal_name)
                
        else:
            response.success = False
            response.message = 'No message recieved'
        
        return response

def main():
    rclpy.init()
    number_goals = int(input("Enter the number of goals: "))
    robot_goals = []
    for i in range(1,(number_goals+1)):
        print("Available goals:\n1. Red Pringles\n2. Green Pringles\n")
        user_goal = input("Choose 1 or 2: ")
        if user_goal == '1':
            user_goal = 'redpringles'
        else: user_goal = 'greenpringles'
        robot_goals.append(user_goal)
        print(f'Goal Number {i} is registered')
    print("You have reached your goal limit.")
    print(f"Available goals: {robot_goals}.\nYou can now assign these goals to your robots.")
    task_allocator = TaskAllocatorService(robot_goals)
    rclpy.spin(task_allocator)
    task_allocator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()