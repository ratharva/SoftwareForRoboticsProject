import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
import cv2 # OpenCV library
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class InferQR(Node):
    def __init__(self):
        """
        Class constructor to set up the node
        """
        # Initiate the Node class's constructor and give it a name
        super().__init__('image_publisher')
        self.image = None
        

        self.counter = 0

        
        # Create the publisher. This publisher will publish an Image
        # to the video_frames topic. The queue size is 10 messages.
        self.publisher_ = self.create_publisher(Twist, '/jackal_velocity_controller/cmd_vel_unstamped', 10)
        
        
        # We will publish a message every 0.1 seconds
        timer_period = 0.1  # seconds
        
        # Create the timer
        # self.timer = self.create_timer(timer_period, self.timer_callback)
            
        # Create a VideoCapture object
        # The argument '0' gets the default webcam.
        # self.cap = cv2.VideoCapture(0)
            
        # # Used to convert between ROS and OpenCV images
        self.br = CvBridge()
        self.subscription = self.create_subscription(String, 'qr_string', self.qr_interpreter, 10)
        self.midpoint = []
        self.depthMap = []
    
    def qr_interpreter(self, msg):
        myQRData = msg.data
        if msg.data == "move_forward":
        
            twist = Twist()
            twist.linear.x = 0.5

            self.publisher_.publish(twist)

        elif msg.data == "turn_clockwise":
            twist = Twist()
            twist.angular.z = -0.5

            self.publisher_.publish(twist)

        elif msg.data == "turn_counterclockwise":
            twist = Twist()
            twist.angular.z = 0.5

            self.publisher_.publish(twist)

        else:
            pass

def main(args=None):

    # Initialize the rclpy library
    rclpy.init(args=args)
    
    # Create the node
    infer_qr = InferQR()
    
    # Spin the node so the callback function is called.
    rclpy.spin(infer_qr)
    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    infer_qr.destroy_node()
    
    # Shutdown the ROS client library for Python
    rclpy.shutdown()
        
if __name__ == '__main__':
    main()
