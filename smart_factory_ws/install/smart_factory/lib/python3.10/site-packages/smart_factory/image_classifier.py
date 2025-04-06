import cv2
from cv_bridge import CvBridge
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from ultralytics import YOLO

    
class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        
        yolo_file = '/home/prethiviraj/ros2/workspaces/Smart_Factory/smart_factory_ws/src/smart_factory/yolo_model/rs2_hardware.pt'
        
        self.camera_id = 0
        self.camera = cv2.VideoCapture(self.camera_id)
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
        
        success,frame = self.camera.read()
        frame = cv2.resize(frame,(820,640),interpolation=cv2.INTER_CUBIC)
        
        if success == True:
            
            self.image_sub = self.bridge.imgmsg_to_cv2(imgmsg)

    
def main():
    rclpy.init()
    image_class = ImagePublisher()
    rclpy.spin(image_class)
    image_class.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
    
        
        