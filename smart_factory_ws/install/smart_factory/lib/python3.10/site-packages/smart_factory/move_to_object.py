import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO
import time
import math
from sensor_msgs.msg import CameraInfo
from geometry_msgs.msg import Twist

class MovetoObject(Node):
    def __init__(self):
        super().__init__('move_to_object')

        self.declare_parameter('camera_centre_x', 80.0)
        self.declare_parameter('camera_centre_y', 60.0)
        self.declare_parameter('distance_threshold', 180)
        self.declare_parameter('angle_threshold', 20.0)
        self.declare_parameter('linear_velocity', 0.2)
        self.declare_parameter('angular_velocity', 0.1)
        self.declare_parameter('search_velocity', 0.1)
        self.declare_parameter('linear_velocity_stop', 0.0)
        self.declare_parameter('angular_velocity_stop', 0.0)
        self.declare_parameter('robot_number',1)

        self.declare_parameter('camera_topic', '/camera/image_raw')
        self.declare_parameter('model_path', '/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/yolo_model/tb3_object.pt')
        self.declare_parameter('camera_pub_topic', '/camera/image_classify')
        self.declare_parameter('vel_pub_topic' '/cmd_vel')
        
        self.robot_name = 'robot'
        self.c_x = 0.0
        self.c_y = 0.0
        self.robot_number = self.get_parameter('robot_number').get_parameter_value().string_value
        self.robot = '/' + self.robot_name + '_' + self.robot_number + '/'
        self.camera_centre_x = self.get_parameter('camera_centre_x').get_parameter_value().double_value
        self.camera_centre_y = self.get_parameter('camera_centre_y').get_parameter_value().double_value
        self.distance_threshold = self.get_parameter('distance_threshold').get_parameter_value().double_value
        self.angle_threshold = self.get_parameter('angle_threshold').get_parameter_value().double_value
        self.object_name = self.get_parameter('object_name').get_parameter_value().string_value
        self.linear_velocity = self.get_parameter('linear_velocity').get_parameter_value().double_value
        self.angular_velocity = self.get_parameter('angular_velocity').get_parameter_value().double_value
        self.search_velocity = self.get_parameter('search_velocity').get_parameter_value().double_value
        self.linear_velocity_stop = self.get_parameter('linear_velocity_stop').get_parameter_value().double_value
        self.angular_velocity_stop = self.get_parameter('angular_velocity_stop').get_parameter_value().double_value
        #self.camera_info_sub = self.create_subscription(CameraInfo,'/camera/camera_info',self.camera_info_callback,10)
        self.camera_topic = self.robot + self.get_parameter('camera_topic').get_parameter_value().string_value
        self.model_path = self.get_parameter('model').get_parameter_value().string_value
        self.camera_pub_topic = self.robot + self.get_parameter('camera_pub_topic').get_parameter_value().string_value
        self.vel_pub_topic = self.robot + self.get_parameter('vel_pub_topic').get_parameter_value().string_value
        
        
        self.camera_sub = self.create_subscription(Image,self.camera_topic,self.classify_callback,10)
        self.cam_pub = self.create_publisher(Image,self.camera_pub_topic,10)
        self.velocity_publisher = self.create_publisher(Twist,self.vel_pub_topic,10)
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
                print(f'distance:{distance}')
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
                self.robot_forward() 
        else:
            self.robot_stop()
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
    

    # def camera_info_callback(self,msg):
    #     self.camera_centre_x = msg.width/2
    #     self.camera_centre_y = msg.height/2


def main():
    rclpy.init()
    move_to_object = MovetoObject()
    rclpy.spin(move_to_object)
    move_to_object.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()