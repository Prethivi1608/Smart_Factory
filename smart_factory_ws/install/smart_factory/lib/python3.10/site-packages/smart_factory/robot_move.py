import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class RobotMove(Node):
    def __init__(self):
        super().__init__('robot_move')

        self.tb1_velocity_pub = self.create_publisher(Twist,'/cmd_vel', 10)
        self.tb2_velocity_pub = self.create_publisher(Twist,'/TB3_2/cmd_vel', 10)
        self.timer = self.create_timer(0.5,self.velocity_callback)
        self.velocity_msg = None

    def robot_move_forward(self):
        self.velocity_msg = Twist()
        self.velocity_msg.linear.x = 0.1
        self.tb1_velocity_pub.publish(self.velocity_msg)

    def robot_stop(self):
        self.stop_msg = Twist()
        self.stop_msg.linear.x = 0.0
        self.tb1_velocity_pub.publish(self.stop_msg)
    
    def robot_left(self):
        self.left_msg = Twist()
        self.left_msg.linear.x = 0.05
        self.left_msg.angular.z = 0.1
        self.tb1_velocity_pub.publish(self.left_msg)   

    def velocity_callback(self):
        self.robot_move_forward()
        time.sleep(1)
        self.robot_left()
        time.sleep(2)
        self.robot_stop()
        time.sleep(1)

def main():
    rclpy.init()
    robot_move = RobotMove()
    rclpy.spin(robot_move)
    robot_move.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()