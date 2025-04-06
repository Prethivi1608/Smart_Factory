from rclpy.node import Node
import rclpy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from ultralytics import YOLO


class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        
        self.camera_id = 0
        
        self.image_topic = 'camera/image_process'
        self.image_pub = self.create_publisher(Image,self.image_topic,10)
        self.timer = self.create_timer(0.5,self.image_callback)
        self.model = YOLO('/home/prethiviraj/ros2/workspaces/Smart_Factory/smart_factory_ws/src/smart_factory/yolo_model/rs2_hardware.pt')
        self.bridge = CvBridge()
        
        
    def image_callback(self):
        
        self.results = self.model.track(source = self.camera_id)
        annotated_frame = self.results[0].plot()
        
        self.pub_image = self.bridge.cv2_to_imgmsg(annotated_frame)
        
        self.image_pub.publish(self.pub_image)
        
        
        
def main():
    rclpy.init()
    image_publisher = ImagePublisher()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()
        
        
if __name__ == '__main__':
    main()
        