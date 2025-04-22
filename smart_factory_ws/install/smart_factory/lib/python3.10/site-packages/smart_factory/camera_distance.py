import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO
from geometry_msgs.msg import Twist
import time
import math

class DistanceCalculator(Node):
    def __init__(self):
        super().__init__('camera_classifier')


        self.camera_topic = '/camera/image_raw'
        self.model_path = '/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/runs/detect/train5/weights/best.pt'
        self.camera_sub = self.create_subscription(Image,self.camera_topic,self.classify_callback,10)
        self.velocity_pub = self.create_publisher(Twist,'/cmd_vel',10)
        self.bridge = CvBridge()
        self.model = YOLO(self.model_path)
        
    
    def classify_callback(self,img_msg):
        image = self.bridge.imgmsg_to_cv2(img_msg)
        
        
        self.results = self.model.track(image)
        bounding_box = self.results[0]
        for box in bounding_box.boxes:
            x1,y1,x2,y2 = box.xyxy.tolist()[0]
            distance = self.distance_to(x1,x2,y1,y2)
            print(distance)
            #self.velocity_callback(distance)
    
    def velocity_callback(self,distance):
        vel_msg = Twist()
        # if distance>450:
        #     vel_msg.linear.x = 0.00
        print(distance)
        #     self.velocity_pub.publish(vel_msg)
        # else:
        #     vel_msg.linear.x = 0.01
        #     self.velocity_pub.publish(vel_msg)

    
    def distance_to(self,x1,x2,y1,y2):
        return (math.sqrt(((x2-x1)**2)+((y2-y1)**2)))



def main():
    rclpy.init()
    camera_distance = DistanceCalculator()
    rclpy.spin(camera_distance)
    camera_distance.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()