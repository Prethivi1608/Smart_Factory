import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO
import time
import math
from sensor_msgs.msg import CameraInfo
from geometry_msgs.msg import Twist

class CameraClassfier(Node):
    def __init__(self):
        super().__init__('camera_classifier')


        self.camera_centre_x = 0.0
        self.camera_centre_y = 0.0
        self.c_x = 0.0
        self.c_y = 0.0

        self.camera_info_sub = self.create_subscription(CameraInfo,'/camera/camera_info',self.camera_info_callback,10)
        self.camera_topic = '/camera/image_raw'
        self.model_path = '/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/yolo_model/smart_fact.pt'
        self.camera_sub = self.create_subscription(Image,self.camera_topic,self.classify_callback,10)
        self.cam_pub = self.create_publisher(Image,'/camera/image_classify',10)
        self.velocity_publisher = self.create_publisher(Twist,'/cmd_vel',10)
        self.bridge = CvBridge()
        self.model = YOLO(self.model_path)
        

    
    def classify_callback(self,img_msg):
        
        image = self.bridge.imgmsg_to_cv2(img_msg)
        self.results = self.model.track(image)
        box_id = self.results[0].boxes.id
        if box_id is None:
            self.robot_search()
        else:
            self.annotated_image = self.results[0].plot()
            image_pub = self.bridge.cv2_to_imgmsg(self.annotated_image)
            self.cam_pub.publish(image_pub)
            bounding_box = self.results[0]
            for box in bounding_box.boxes:
                class_id = int(box.cls[0].item())
                class_name = self.model.names[class_id]
                print(f'Detected Object:{class_name}')
                x1,y1,x2,y2 = box.xyxy.tolist()[0]
                distance = self.distance_to(x1,x2,y1,y2)
                self.c_x,self.c_y,w,h= box.xywh.tolist()[0]
                if self.c_x == None:
                    self.get_logger().info('No value')
                else:  
                    if class_name == 'bowl':
                        self.velocity_callback(self.c_x,distance)
                    else:
                        self.robot_search()


    def velocity_callback(self,c_x,distance):
        if distance < 450:
            if c_x>self.camera_centre_x+50:
                self.robot_right()
            elif c_x<self.camera_centre_x-50:
                self.robot_left()
            else:
                self.robot_forward() 
        else:
            self.robot_stop()
            self.get_logger().info('Reached near the object')
            
    def robot_stop(self):
        vel_msg = Twist()
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 0.0
        self.velocity_publisher.publish(vel_msg)
    
    def robot_forward(self):
        vel_msg = Twist()
        vel_msg.linear.x = 0.5
        vel_msg.angular.z = 0.0
        self.velocity_publisher.publish(vel_msg)
    
    def robot_left(self):
        vel_msg = Twist()
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 0.1
        self.velocity_publisher.publish(vel_msg)
    
    def robot_right(self):
        vel_msg = Twist()
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = -0.1
        self.velocity_publisher.publish(vel_msg)
    
    def robot_search(self):
        vel_msg = Twist()
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 0.3
        self.velocity_publisher.publish(vel_msg)


    def distance_to(self,x1,x2,y1,y2):
        return (math.sqrt(((x2-x1)**2)+((y2-y1)**2)))
    

    def camera_info_callback(self,msg):
        self.camera_centre_x = msg.width/2
        self.camera_centre_y = msg.height/2


def main():
    rclpy.init()
    camera_classifier = CameraClassfier()
    rclpy.spin(camera_classifier)
    camera_classifier.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()