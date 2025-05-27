import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger

class TextClient(Node):
    def __init__(self):
        super().__init__('text_client')
        self.client = self.create_client(Trigger, 'send_text')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

        self.req = Trigger.Request()

    def send_text(self, text):
        self.req.data = text
        future = self.client.call_async(self.req)
        future.add_done_callback(self.callback)

    def callback(self, future):
        response = future.result()
        self.get_logger().info(f'Service Response: {response.message}')

def main(args=None):
    rclpy.init(args=args)
    text_client = TextClient()

    text = "Hello from Client!"
    text_client.send_text(text)

    rclpy.spin_once(text_client)

if __name__ == '__main__':
    main()
