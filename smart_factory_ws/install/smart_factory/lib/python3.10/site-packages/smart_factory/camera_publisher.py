import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge


class CameraPublisher(Node):
    def __init__(self):
        super().__init__('camera_publisher')

        self.camera_pub_topic = '/camera/image_webcam'
        self.camera_pub = self.create_publisher(Image,self.camera_pub_topic,10)
        self.timer = self.create_timer(0.1,self.camera_callback)

        self.camera_id = 2
        self.camera = cv2.VideoCapture(self.camera_id)
        self.bridge = CvBridge()

    def camera_callback(self):
        
        success,frame = self.camera.read()

        if success == True:
            image_msg = self.bridge.cv2_to_imgmsg(frame)

            self.camera_pub.publish(image_msg)
    
def main():
    rclpy.init()
    camera_publisher = CameraPublisher()
    rclpy.spin(camera_publisher)
    camera_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


            
