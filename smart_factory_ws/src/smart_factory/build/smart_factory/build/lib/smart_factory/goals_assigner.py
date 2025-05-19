import rclpy
from rclpy.node import Node
from smart_factory_services.srv import TaskAllocation
from nav_msgs.msg import Odometry
import math
import time
import random

class GoalAllocator(Node):
    def __init__(self,assign_choose,pick_goals,object_goals,drop_goals):
        super().__init__(f'goal_allocator')
        
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

    
    def odom_callback(self,msg):
        position = msg.pose.pose.position
        self.robot_x = position.x
        self.robot_y = position.y
    

    def distance_between_points(self,x1,y1,x2,y2):
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))


# def main():
#     goal_assigner = GoalAssigner()
#     goal_assigner.get_goal()

# if __name__ == '__main__':
#     main()