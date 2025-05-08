import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger  # You can use any service type

class TextService(Node):
    def __init__(self):
        super().__init__('text_service')
        self.srv = self.create_service(Trigger, 'send_text', self.send_text_callback)

    def send_text_callback(self, request, response):
        text = request.data
        self.get_logger().info(f'Received text: {text}')
        response.success = True
        response.message = 'Text received successfully'
        return response

def main(args=None):
    rclpy.init(args=args)
    text_service = TextService()
    rclpy.spin(text_service)

if __name__ == '__main__':
    main()
