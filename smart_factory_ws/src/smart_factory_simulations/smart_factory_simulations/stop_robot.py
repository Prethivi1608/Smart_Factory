import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile, ReliabilityPolicy


class DetectObject(Node):
    def __init__(self,robot_number):
        super().__init__('detect_object')

        qos = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)

        self.robot_number = robot_number
        self.robot = '/robot' + '_' + str(self.robot_number)
        self.scan_topic = self.robot + '/scan'
        self.vel_topic = self.robot + '/cmd_vel'
        self.detect_sub = self.create_subscription(LaserScan,self.scan_topic,self.scan_callback,qos)
        self.object_distance = {}
        self.velocity_publisher = self.create_publisher(Twist,self.vel_topic,10)
        
        self.left_angle = 358
        self.right_angle = 2
        self.ranges = []
        self.obstacle = False

    def scan_callback(self,msg):
        self.ranges = msg.ranges
        for i in range(len(self.ranges)):
            if i>self.left_angle or i<self.right_angle:
                if self.ranges[i]<0.5:
                    self.obstacle = True
                    self.operate_robot()
                else:
                    self.obstacle = False
                    self.operate_robot()
        
    
    def operate_robot(self):
        while self.obstacle:
            self.robot_stop()
        
        self.robot_forward()

    def robot_forward(self):
        print('Robot Moving')
        velocity_msg = Twist()
        velocity_msg.linear.x = 0.2

        self.velocity_publisher.publish(velocity_msg)
        
    
    def robot_stop(self):
        print("Robot Stopped..")
        velocity_msg = Twist()
        velocity_msg.linear.x = 0.0

        self.velocity_publisher.publish(velocity_msg)
        


def main():
    if not rclpy.ok():
        rclpy.init()
    number = 1
    detect_object = DetectObject(number)
    rclpy.spin(detect_object)
    detect_object.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()