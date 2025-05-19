import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile, ReliabilityPolicy


class DetectObject(Node):
    def __init__(self,robot_number):
        super().__init__('detect_object')

        qos = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)

        self.robot_number = robot_number
        self.robot = '/robot' + '_' + str(self.robot_number)
        self.scan_topic = self.robot + '/scan'
        self.detect_sub = self.create_subscription(LaserScan,self.scan_topic,self.scan_callback,qos)
        self.object_distance = {}
        
        self.left_angle = 350
        self.right_angle = 10


    def scan_callback(self,msg):
        for i in range(len(msg.ranges)):
            if msg.ranges[i] < 1.0:
                if i<self.left_angle and i>self.right_angle:
                    print("Stopping")
                else:
                    print('Moving')

def main():
    if not rclpy.ok():
        rclpy.init()
    number = 2
    detect_object = DetectObject(number)
    rclpy.spin(detect_object)
    detect_object.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()