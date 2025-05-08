import rclpy
from rclpy.node import Node
from smart_factory_services.srv import TaskAllocation
from nav_msgs.msg import Odometry
import math

class TaskAllocatorService(Node):
    def __init__(self,assign_choose,robot_goals):
        super().__init__('task_allocator_service')

        self.task_service = self.create_service(TaskAllocation,'allocate_task',self.allocate_callback)
        self.goals = robot_goals
        self.assign_choose = assign_choose
        self.robot_x = None
        self.robot_y = None

    def allocate_callback(self,request,response):
        number = request.robot_number

        if number is not None:
            response.success = True
            
            self.robot = '/' + 'robot_' + str(number)
            self.pos_sub_topic = '/odom'
            
            if self.assign_choose == 1:
                if len(self.goals) == 0:
                    response.message = f'No goals to assign for robot_{number}'
                    self.get_logger().info('No goals to assign')
                else:
                    goal_name = self.goals[0]
                    response.object_name = goal_name
                    response.message = f'{goal_name} goal is assigned to robot_{number}'
                    del self.goals[0]
                    self.get_logger().info(f'Available goals: {len(self.goals)}')
                
            else:
                self.pos_subscriber = self.create_subscription(Odometry,self.pos_sub_topic,self.odom_callback,10)
                minimum_distance = 99999999
                best_goal = []
                for goal in self.goals:
                    distance = self.distance_between_points(goal[0],goal[1],self.robot_x,self.robot_y)
                    if distance < minimum_distance:
                        minimum_distance = distance
                        best_goal = goal
                
                response.message = f'{best_goal} goal is assigned to robot_{number}'
                self.goals.remove(best_goal)
                print(len(self.goals))
                 
        else:
            response.success = False
            response.message = 'No message recieved'
        
        return response
    
    def odom_callback(self,msg):
        position = msg.pose.pose.position
        self.robot_x = position.x
        self.robot_y = position.y
    

    def distance_between_points(self,x1,y1,x2,y2):
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

def main():
    rclpy.init()
    
    
    assign_chooser = int(input("How do you want to assign the goals to robots:\n1. By Index\n2. By Distance\n"))
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
    
    
    task_allocator = TaskAllocatorService(assign_chooser,robot_goals)
    rclpy.spin(task_allocator)
    task_allocator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()