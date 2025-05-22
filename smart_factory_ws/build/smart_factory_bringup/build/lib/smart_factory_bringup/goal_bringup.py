import rclpy
from rclpy.node import Node

from smart_factory_services.srv import TaskAllocation

class GoalAssigner(Node):
    def __init__(self):
        super().__init__('goal_assigner')
        self.task_service = self.create_service(TaskAllocation,'allocate_task',self.allocate_callback)
        self.assign_chooser = int(input("How do you want to assign the goals to robots:\n1. By Index\n2. By Distance\n"))
        self.number_goals = int(input("Enter the number of goals: "))
        self.pick_goals = []
        self.object_goals = []
        self.drop_goals = []
        self.number = None

    def get_goal(self):
        
        for i in range(1,(self.number_goals+1)):
            print("Choose the pickup location:\n1. Shelf 1\n2. Shelf 2\n")
            pick_goal = input("Choose 1 or 2: ")
            if pick_goal == '1':
                pick_goal = [-0.994065,0.600851]
            else: 
                pick_goal = [0.8218,0.0774]
            
            self.pick_goals.append(pick_goal)

            print("Choose the object to pickup:\n1. Red Pringles\n2. Green Pringles\n") 
            goal_obj = input("Choose 1 or 2: ")
            if goal_obj == '1':
                goal_obj ='redpringles'
            else:
                goal_obj = 'greenpringles'
            
            self.object_goals.append(goal_obj)
            
            print("Choose the drop location:\n1. Shelf 1\n2. Shelf 2\n")
            drop_goal = input("Choose 1 or 2: ")
            if drop_goal == '1':
                drop_goal = [-0.994065,0.600851]
            else: 
                drop_goal = [0.8218,0.0774]

            if pick_goal == drop_goal:
                print('Pick and drop locations are same. Please choose different drop location!')
            else:
                self.drop_goals.append(drop_goal)
            
            print(f'Goal Number {i} is registered')
        
        print("You have reached your goal limit.")
        print(f"Pickup point: {self.pick_goals},Objects: {self.object_goals} Drop points: {self.drop_goals},.\nYou can now assign these goals to your robots.")

        self.check_request()

    def allocate_callback(self,request,response):
        self.number = request.robot_number

        if self.number is not None:
            response.success = True

    def check_request(self):
        if self.number is not None:
            self.assign_goals()

        else:
            self.get_logger().info('Waiting for robot')