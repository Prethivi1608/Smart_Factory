import rclpy
from rclpy.node import Node

import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image


class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        
        self.camera_name = 0
        self.bridge = CvBridge()
        self.camera = cv2.VideoCapture(self.camera_name)
        
        self.publish_topic = "/camera/image_raw"
        self.image_pub = self.create_publisher(Image,self.publish_topic,10)
        self.timer = self.create_timer(0.5,self.image_callback)
    
    def image_callback(self):
        sucess,frame = self.camera.read()
        
        if sucess == True:
            
            img_msg = self.bridge.cv2_to_imgmsg(frame)
            
            self.image_pub.publish(img_msg)
            
def main():
    rclpy.init()
    image_publish = ImageSubscriber()
    rclpy.spin(image_publish)
    image_publish.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
            
            