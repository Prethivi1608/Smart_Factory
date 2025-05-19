import rclpy
from sensor_msgs.msg import CameraInfo
from rclpy.node import Node


class ClassInfo(Node):
    def __init__(self):
        super().__init__('camera_info')

        self.camera_info_sub = self.create_subscription(CameraInfo,'/camera/camera_info',self.camera_info_callback,10)

    def camera_info_callback(self,msg):
        centre_x = msg.width/2
        centre_y = msg.height/2

        self.get_logger().info(f'(x,y):{centre_x},{centre_y}')
    

def main():
    rclpy.init()
    camera_info_ = ClassInfo()
    rclpy.spin(camera_info_)
    camera_info_.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    