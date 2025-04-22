import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO
import time
import math

class CameraClassfier(Node):
    def __init__(self):
        super().__init__('camera_classifier')


        self.camera_topic = '/camera/image_raw'
        self.model_path = '/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/yolo_model/tb3_object.pt'
        self.camera_sub = self.create_subscription(Image,self.camera_topic,self.classify_callback,10)
        self.cam_pub = self.create_publisher(Image,'/camera/image_classify',10)
        self.bridge = CvBridge()
        self.model = YOLO(self.model_path)
        

    
    def classify_callback(self,img_msg):
        image = self.bridge.imgmsg_to_cv2(img_msg)
        self.results = self.model.track(image)
        self.annotated_image = self.results[0].plot()
        image_pub = self.bridge.cv2_to_imgmsg(self.annotated_image)
        self.cam_pub.publish(image_pub)
    


def main():
    rclpy.init()
    camera_classifier = CameraClassfier()
    rclpy.spin(camera_classifier)
    camera_classifier.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()