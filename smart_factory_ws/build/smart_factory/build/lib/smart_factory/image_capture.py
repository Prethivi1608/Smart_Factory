import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import time

class ImageCapture(Node):
    def __init__(self):
        super().__init__('image_capture_node')
        self.bridge = CvBridge()
        
        self.image_subscriber = self.create_subscription(Image,'/camera/image_raw',self.image_callback,10)
        
        self.counter=0

        self.capture_rate = 0.25
        
    def image_callback(self,ImgMessage):    
        self.image = self.bridge.imgmsg_to_cv2(ImgMessage)
        path = '/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/Camera_3'
        file_name = f'{path}/image_{self.counter}.jpg'
        cv2.imwrite(file_name,self.image)
        time.sleep(self.capture_rate)
        self.get_logger().info(f'{self.counter} images has been captured.')
        self.counter+=1
        
            
def main():
    rclpy.init()
    image_capture = ImageCapture()
    rclpy.spin(image_capture)
    image_capture.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
    
        