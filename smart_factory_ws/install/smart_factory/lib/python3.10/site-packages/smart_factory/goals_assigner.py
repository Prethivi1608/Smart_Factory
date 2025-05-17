import rclpy
from rclpy.node import Node
from smart_factory_services.srv import TaskAllocation
from nav_msgs.msg import Odometry
import math
import time
import random

class TaskAllocatorService(Node):
    def __init__(self,assign_choose,pick_goals,object_goals,drop_goals):
        super().__init__(f'task_allocator_service')
        
        self.task_service = self.create_service(TaskAllocation,'allocate_task',self.allocate_callback)
        self.pos_sub_topic = '/odom'
        self.pick_goals = pick_goals
        self.object_goals = object_goals
        self.drop_goals = drop_goals
        self.assign_choose = assign_choose
        self.robot_x = None
        self.robot_y = None
        self.pos_subscriber = self.create_subscription(Odometry,self.pos_sub_topic,self.odom_callback,10)
        self.number = None
        self.robot = None
        

        self.robot = '/' + 'robot_' + str(self.number)
        
        if self.number is None:
            self.get_logger().info('Waiting for the robot..')
        else:
            self.pos_sub_topic = self.robot + '/odom'

    def allocate_callback(self,request,response):
        self.number = request.robot_number

        if self.number is not None:
            response.success = True
            
            if self.assign_choose == 1:
                if len(self.pick_goals) == 0 or len(self.drop_goals) == 0:
                    response.message = f'No goals to assign for robot_{self.number}'
                    self.get_logger().info('No goals to assign..')
                    self.get_goal()
                else:
                    response.available_goals = len(self.pick_goals)
                    pick_goal = self.pick_goals[0]
                    object_goal = self.object_goals[0]
                    drop_goal = self.drop_goals[0]
                    response.pick_goal = pick_goal
                    response.object_goal = object_goal
                    response.drop_goal = drop_goal
                    response.message = f'Robot-{self.number} is picking {object_goal} from {pick_goal} and dropping at {drop_goal}'

                    del self.pick_goals[0]
                    del self.object_goals[0]
                    del self.drop_goals[0]
                
            else:
                if len(self.pick_goals) == 0:
                    response.message = f'No goals to assign for robot_{self.number}'
                    self.get_logger().info('No goals to assign')
                    self.get_goal()
                
                else:
                    response.available_goals = len(self.pick_goals)
                    minimum_distance = 99999999
                    best_pick_goal = []
                    best_drop_goal = []
                    drop_goal_index = None
                    object_goal = self.object_goals[0]
                    for pick_goal,i in enumerate(self.pick_goals):
                        distance = self.distance_between_points(pick_goal[0],pick_goal[1],self.robot_x,self.robot_y)
                        if distance < minimum_distance:
                            minimum_distance = distance
                            best_pick_goal = pick_goal
                            best_drop_goal = self.drop_goals
                            drop_goal_index = i
                    
                    response.pick_goal = best_pick_goal
                    response.object_name = object_goal
                    response.drop_goal = drop_goal
                    response.message = f'Robot-{self.number} is picking {object_goal} from {best_pick_goal} and dropping at {best_drop_goal}'
                    self.pick_goals.remove(best_pick_goal)
                    del self.drop_goals[drop_goal_index]
                    del self.object_goals[0]
                 
        else:
            response.success = False
            response.message = 'No message recieved'
        
        return response
    
    def get_goal(self):
        get_goal = GoalAssigner()
        get_goal.get_goal()

    
    def odom_callback(self,msg):
        position = msg.pose.pose.position
        self.robot_x = position.x
        self.robot_y = position.y
    

    def distance_between_points(self,x1,y1,x2,y2):
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    
    
    
class GoalAssigner():
    def __init__(self):
    
        self.assign_chooser = int(input("How do you want to assign the goals to robots:\n1. By Index\n2. By Distance\n"))
        self.number_goals = int(input("Enter the number of goals: "))
        self.pick_goals = []
        self.object_goals = []
        self.drop_goals = []

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

        self.call_task_service()

    def call_task_service(self):
        if not rclpy.ok():
            rclpy.init()
        task_allocator = TaskAllocatorService(self.assign_chooser,self.pick_goals,self.object_goals,self.drop_goals)
        
        rclpy.spin(task_allocator)
        
        task_allocator.destroy_node()


def main():
    goal_assigner = GoalAssigner()
    goal_assigner.get_goal()

if __name__ == '__main__':
    main()