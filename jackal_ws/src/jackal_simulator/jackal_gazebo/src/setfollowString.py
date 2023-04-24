import rclpy
from std_msgs.msg import String
import sys


class StringPublisher:
    def __init__(self, node_name='string_publisher', topic_name='toFollowString', publish_rate=10):
        self.node = rclpy.create_node(node_name)
        self.publisher = self.node.create_publisher(String, topic_name, 10)
        self.msg = String()
        self.msg.data = sys.argv[1]
        self.timer_period = 1 / publish_rate
        self.timer = self.node.create_timer(self.timer_period, self.publish)

    def publish(self):
        self.publisher.publish(self.msg)
        self.node.get_logger().info('Publishing: "%s"' % self.msg.data)

    def spin(self):
        rclpy.spin(self.node)

    def destroy(self):
        self.node.destroy_node()
        rclpy.shutdown()


def main():
    publisher = StringPublisher()
    publisher.spin()
    publisher.destroy()


if __name__ == '__main__':
    rclpy.init()
    main()

    