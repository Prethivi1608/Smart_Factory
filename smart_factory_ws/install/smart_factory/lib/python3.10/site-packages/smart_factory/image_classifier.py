import cv2
from cv_bridge import CvBridge
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from ultralytics import YOLO
import os

class ImageClassifier(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        
        yolo_file = '/home/prethiviraj/ros2/workspaces/Smart_Factory/smart_factory_ws/src/smart_factory/yolo_model/rs2_hardware.pt'
        
        self.image_topic = '/camera/image_process'
        self.bridge = CvBridge()
        self.image_pub = self.create_publisher(Image,self.image_topic,10)
        self.timer = self.create_timer(0.5,self.image_callback)
        self.model = YOLO(yolo_file)
        
    def image_callback(self):

        self.results=self.model.track(source=0)
        annotated_frame = self.results[0].plot()

        self.pub_image = self.bridge.cv2_to_imgmsg(annotated_frame)
        
        self.image_pub.publish(self.pub_image)
    
def main():
    rclpy.init()
    image_class = ImageClassifier()
    rclpy.spin(image_class)
    image_class.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
    
        
        