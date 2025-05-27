import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO
import time
import math
from sensor_msgs.msg import CameraInfo
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import random
import cv2
from rclpy.qos import QoSProfile, ReliabilityPolicy

class MovetoObject(Node):
    def __init__(self,robot_number,object_name):
        super().__init__(f'move_to_object_{random.randint(0,120)}')
        
        qos = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)
        self.robot_name = 'robot'
        self.c_x = 0.0
        self.c_y = 0.0
        self.robot_number = robot_number
        self.robot = '/' + self.robot_name + '_' + str(self.robot_number)
        self.camera_centre_x= 80.0
        self.camera_centre_y= 60.0
        self.distance_threshold= 180
        self.angle_threshold= 40.0
        self.linear_velocity= -0.25
        self.angular_velocity= 0.15
        self.search_velocity= 0.15
        self.linear_velocity_stop= 0.0
        self.angular_velocity_stop= 0.0
        self.task_status = 'Running'
        self.object_name = object_name
        self.obstacle = False
        

        self.camera_topic = self.robot + '/camera/image_raw'
        self.model_name = 'tb3_object.pt'
        self.model_path = '/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/yolo_model/' + self.model_name
        self.camera_pub_topic = self.robot + '/camera/image_classify'
        self.vel_pub_topic = self.robot + '/cmd_vel'
        self.scan_topic = self.robot + '/scan'
        
        self.cam_pub = self.create_publisher(Image,self.camera_pub_topic,10)
        self.cam_sub = self.create_subscription(Image,self.camera_topic,self.classify_callback,10)
        self.laser_sub = self.create_subscription(LaserScan,self.scan_topic,self.scan_callback,qos)
        self.velocity_publisher = self.create_publisher(Twist,self.vel_pub_topic,10)
        self.bridge = CvBridge()
        self.model = YOLO(self.model_path)

        self.left_angle = 190
        self.right_angle = 170
    
    def scan_callback(self,msg):
        self.ranges = msg.ranges
        for i in range(len(self.ranges)):
            if i<self.left_angle or i>self.right_angle:
                if self.ranges[i]<0.5:
                    self.obstacle = False
                else:
                    self.obstacle = True
        
    def classify_callback(self,img_msg):
        
        image = self.bridge.imgmsg_to_cv2(img_msg,desired_encoding='bgr8') 
        # image = cv2.flip(flipped_image, 0)
        self.results = self.model.track(image)
        box_id = self.results[0].boxes.id
        if box_id is None:
            self.robot_search()
        else:
            self.task_status = 'Object Found'
            self.get_logger().info('Object Found')
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
                    if class_name == self.object_name:
                        self.velocity_callback(self.c_x,distance)
                    else:
                        self.robot_search()
    
    def velocity_callback(self,c_x,distance):
        
        if distance < self.distance_threshold:
            if c_x>(self.camera_centre_x+self.angle_threshold):
                self.robot_right()

            elif c_x<(self.camera_centre_x-self.angle_threshold):
                self.robot_left()

            else:
                if self.obstacle:
                    self.robot_stop()
                    print('Robot obstacle')
                else:
                    self.robot_forward()
        else:
            self.robot_stop()
            self.task_status = 'Reached near the object'
            self.get_logger().info('Reached near the object')
            
    def robot_stop(self):
        vel_msg = Twist()
        vel_msg.linear.x = self.linear_velocity_stop
        vel_msg.angular.z = self.angular_velocity_stop
        self.velocity_publisher.publish(vel_msg)
    
    def robot_forward(self):
        vel_msg = Twist()
        vel_msg.linear.x = self.linear_velocity
        vel_msg.angular.z = self.angular_velocity_stop
        self.velocity_publisher.publish(vel_msg)
    
    def robot_left(self):
        vel_msg = Twist()
        vel_msg.linear.x = self.linear_velocity_stop
        vel_msg.angular.z = self.angular_velocity
        self.velocity_publisher.publish(vel_msg)
    
    def robot_right(self):
        vel_msg = Twist()
        vel_msg.linear.x = self.linear_velocity_stop
        vel_msg.angular.z = -self.angular_velocity
        self.velocity_publisher.publish(vel_msg)
    
    def robot_search(self):
        vel_msg = Twist()
        vel_msg.linear.x = self.linear_velocity_stop
        vel_msg.angular.z = self.search_velocity
        self.velocity_publisher.publish(vel_msg)


    def distance_to(self,x1,x2,y1,y2):
        return (math.sqrt(((x2-x1)**2)+((y2-y1)**2)))
    

def main():
    if not rclpy.ok():
        rclpy.init()
    move_to_object = MovetoObject()
    rclpy.spin(move_to_object)
    move_to_object.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()