import subprocess
import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import String


from smart_factory_services.srv import TaskAllocation
from smart_factory.smart_factory.request_goal import RequestGoal
from smart_factory.smart_factory.go_to_goal import Navigation
from smart_factory.smart_factory.move_to_object import MovetoObject
# from smart_factory_services.srv import RobotStatus


class Robot(Node):
    def __init__(self,number,robot_id,camera_format):
        super().__init__(f'robot_{robot_id}')

        self.robot_number = number # Number on the namespace
        self.robot_id = robot_id # Id of the turtlebot. Number on the top.
        self.robot = f'/robot_{str(self.robot_number)}' 
        self.camera_format = camera_format

        self.home_position = []
        self.pick_point = []
        self.pick_object = []
        self.drop_point = []

    def robot_startup(self):
        
        ssh_command = ('')

        self.ask_for_goal()
    
    def ask_for_goal(self):

        # Ask for the goal method -- Once the robot starts
        
        start_time = time.time()
        duration = 10
        request_goal = RequestGoal(self.robot) 
        status = request_goal.send_request(self.robot_number)

        while time.time() - start_time < duration:
            rclpy.spin_once(request_goal,timeout_sec=0.1) 

        if status == 'Goals Assigned':
            self.pick_point = request_goal.pick_goal
            self.drop_point = request_goal.drop_goal
            self.pick_object = request_goal.object_goal
            self.navigate_to_pickup(self.pick_point[0],self.pick_point[1],self.robot) # If goals assigned navigate to pick up point
        
        else:
            self.get_logger().info('No goals for the robot !!')
            self.stand_by() # Go to standby if no goals assigned

        request_goal.destroy_node()

    def stand_by(self):
        
        self.get_logger().info('Standby Mode:\n')
        standby_response = input('1. Try Again for goals \n2. Shutdown the robot\n') # Ask the user for response.
        if standby_response == '1':
            self.ask_for_goal() # Call the ask for goal.
        else:
            self.shutdown() # Shuts down the robot

    def shutdown(self):
        # Function to shut down the robot

        self.navigate_to_home(self.home_position[0],self.home_position[1],self.robot)

        self.get_logger().info(f'Shutting down the robot_{self.robot_id}!!')
        self.destroy_node()
        rclpy.shutdown()
    
    def navigate_to_pickup(self,goal_x,goal_y,robot):
        # Function to navigate to pick up point
        
        self.get_logger().info('Moving to pickup location...')
        
        start_time = time.time()
        duration = 20
        go_goal = Navigation(goal_x,goal_y,robot)

        while time.time() - start_time < duration:
            rclpy.spin_once(go_goal,timeout_sec=0.1)
        
        if go_goal.done == True:
            self.pick_up_object(self.robot_number,self.pick_object) # Call the pick up object function
        
        else:
            response = input('1. Retry \n2. Cancel')
            if response == '1': # User to give response. 
                self.navigate_to_pickup(self.pick_point[0],self.pick_point[1],self.robot) # Try to navigate the robot again
            else:
                self.ask_for_goal() # Request for the next goal.
        
        go_goal.destroy_node()

    
    def navigate_to_home(self,goal_x,goal_y,robot):
        # Function to navigate to pick up point
        
        self.get_logger().info('Moving to Home Position...')
        
        start_time = time.time()
        duration = 20
        go_goal = Navigation(goal_x,goal_y,robot)

        while time.time() - start_time < duration:
            rclpy.spin_once(go_goal,timeout_sec=0.1)
        
        if go_goal.done == True:
            return
        
        else:
            response = input('1. Retry \n2. Cancel')
            if response == '1': # User to give response. 
                self.navigate_to_home(self.pick_point[0],self.pick_point[1],self.robot) # Try to navigate the robot again
            else:
                print("Can't reach the home position.!")
                return
        
        go_goal.destroy_node()

    def pick_up_object(self,robot_number,object_name):
        # Function to pick up the object

        self.get_logger().info(f'Picking {object_name}...')

        start_time = time.time()

        duration = 50
        move_to_object = MovetoObject(robot_number,object_name)

        while time.time() - start_time < duration:
            rclpy.spin_once(move_to_object,timeout_sec=0.1)

         # If success: navigate to drop location 
         # else: ask for next goal

        if move_to_object.task_status == 'Reached near the object': 
            self.navigate_to_drop(self.drop_point[0],self.drop_point[1],self.robot)
        
        else:
            self.ask_for_goal()
        
        move_to_object.destroy_node()

    def navigate_to_drop(self,goal_x,goal_y,robot):

        self.get_logger().info('Moving to drop location...')

        start_time = time.time()
        duration = 20
        go_goal = Navigation(goal_x,goal_y,robot)

        while time.time() - start_time < duration:
            rclpy.spin_once(go_goal,timeout_sec=0.1)
        
        # If robot reached drop point: ask for the next goal, 
        # else: Ask the user to retry and cancel. 
        # Retry: navigate to drop ; cancel : ask for next goal
        
        if go_goal.done == True:
            self.ask_for_goal()
        
        else:
            response = input('1. Retry \n2. Cancel')
            if response == '1':
                self.navigate_to_drop(self.pick_point[0],self.pick_point[1],self.robot)
            else:
                self.ask_for_goal()
        
        go_goal.destroy_node()


def main():
    rclpy.init()
    robot_id = input('Enter the Robot ID: \n')
    robot_number = input(f'Enter the number of Robot-{robot_id} \n')
    camera_type = input('Choose the camera:\n1. RaspberryPi Camera \n2. Webcam')
    if camera_type == '1':
        camera_format = 'RGB888'
    else:
        camera_format = 'MJPEG'

    robot = Robot(robot_number,robot_id,camera_format)
    rclpy.spin(robot)
    robot.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

    
        
        