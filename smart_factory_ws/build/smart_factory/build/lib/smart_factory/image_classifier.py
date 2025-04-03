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
        super().__init__('image_classifier')
        
        yolo_file = '/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/yolo_model/smart_fact.pt'
        
        self.image_topic = '/camera/image_raw'
        self.image_pub_topic = '/camera/image_process'
        self.image_subscriber = self.create_subscription(Image,self.image_topic,self.image_callback,10)
        self.velocity_publisher = self.create_publisher(Twist,'/cmd_vel',10)
        #self.timer = self.create_timer(0.5,self.move_robot)
        self.bridge = CvBridge()
        self.image_pub = self.create_publisher(Image,self.image_pub_topic,10)
        self.model = YOLO(yolo_file)
        
    def image_callback(self,ImgMsg):
        img_width = 640
        img_height = 480
        self.image = self.bridge.imgmsg_to_cv2(ImgMsg)
        
        
        self.results=self.model.track(source=self.image)
        annotated_frame = self.results[0].plot()

        # self.boxes = self.results[0].boxes.xywh

        # for box in self.boxes:
        #     x,y,w,h = box

        #     print(f"x={x},y={y},width={w},height={h}")
            
        #     while w>50:
        #         self.move_robot()

        
        
        self.pub_image = self.bridge.cv2_to_imgmsg(annotated_frame)
        
        self.image_pub.publish(self.pub_image)
    
    def move_robot(self):
        self.velocity = Twist()
        self.velocity.linear.x = 0.1


        self.velocity_publisher.publish(self.velocity)

def main():
    rclpy.init()
    image_class = ImageClassifier()
    rclpy.spin(image_class)
    image_class.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
    
        
        