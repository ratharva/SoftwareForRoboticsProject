import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image, CameraInfo # Image is the message type
import cv2 # OpenCV library
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
from std_msgs.msg import String
import numpy as np
from geometry_msgs.msg import Twist

class ImagePublisher(Node):
  """
  Create an ImagePublisher class, which is a subclass of the Node class.
  """
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
    self.publisher_ = self.create_publisher(String, 'qr_string', 10)
    self.publisher_2 = self.create_publisher(String, "rect_points", 10)
    self.publisher_3 = self.create_publisher(Twist, 'jackal_velocity_controller/cmd_vel_unstamped', 10)
      
    # We will publish a message every 0.1 seconds
    timer_period = 0.1  # seconds
      
    # Create the timer
    # self.timer = self.create_timer(timer_period, self.timer_callback)
         
    # Create a VideoCapture object
    # The argument '0' gets the default webcam.
    # self.cap = cv2.VideoCapture(0)
         
    # # Used to convert between ROS and OpenCV images
    self.br = CvBridge()
    # self.subscription2 = self.create_subscription(Image, 'd430/depth/image_rect_raw', self.depth_callback, 1)
    # self.subscription3 = self.create_subscription(CameraInfo, 'd430/camera_info', self.camInfo_callback, 1)
    self.subscription = self.create_subscription(Image, 'd430/color/image_raw', self.image_callback, 1)
    # self.subscription4 = self.create_subscription(String, '/toFollowString', self.getFollowString_callback, 1)
    # self.midpoint = []
    self.depthMap = None
    self.K = None
    self.R = None
    self.t = None
    self.toFollowString = None
   
  def image_callback(self, msg):
    myMidpoint = 0
    myQrDetector = cv2.QRCodeDetector()
    """
    Callback function.
    This function gets called every 0.1 seconds.
    """
    try:
      cv_image = self.br.imgmsg_to_cv2(msg, "bgr8")
    except Exception as e:
      self.get_logger().error('Error converting ROS Image to OpenCV: {}'.format(e))
      return
    ret_qr, decoded_info, points, _ = myQrDetector.detectAndDecodeMulti(cv_image)
    if ret_qr:
      for s, p in zip(decoded_info, points):
        if s:
          try:
            myS = String()
            myS.data = s
            self.publisher_.publish(myS)
            print(myS.data)
            print(p)
        #     a = p[0]
        #     b = p[1]
        #     c = p[2]
        #     d = p[3]
        #     myTwist = Twist()
            
        #     intersectionPar = [int((a[0] + b[0] + c[0] + d[0])/4), int((a[1] + b[1] + c[1] + d[1])/4)]
        #     print(intersectionPar)
        #     print("Second Print of depth map: ", self.depthMap)
        #     myDepthVal = self.depthMap[int(intersectionPar[0]), int(intersectionPar[1])]
        #     print("Print of depth val: ", myDepthVal)
        #     #convert to camera co_ordinate system
        #     cameraSys = np.dot(np.linalg.inv(self.K), np.array([intersectionPar[0], intersectionPar[1], 1]))
        #     print("Camera Sys print: ", cameraSys)
        #     #convert to world co_ordinate system
        #     myCamDepth = myDepthVal * cameraSys
        #     print("Camera sys with depth: ", myCamDepth)
        #     print("R Transpose: ", self.R.T)
        #     print("myCamDepth: ", myCamDepth)
        #     print("value of T: ", self.t)
        #     print("Difference", myCamDepth - self.t)
        #     myWorldCoOrds = np.dot(self.R.T, myCamDepth - self.t) #np.dot(self.R.T, myCamDepth) - np.dot(self.R.T, self.t) #
        #     print("World Coordinates: ", myWorldCoOrds)
        #     print(type(myWorldCoOrds))
        #     # print(type(p))
        #     # print(p.shape)
        #     # print("Original Co-ordinates: ", p)
        #     # print("Centre Point: ", intersectionPar)
            
        #     # self.pu
        #     print(s)
        #     # print(type(s))
        #     color = (0, 255, 0)
        #     if a[0] < 400:
        #       #publish message to turn 
        #       myTwist.angular.x = 0.2
        #       self.publisher_3.publish(myTwist)
        #     else:
        #       #publish message to turn right
        #       myTwist.angular.x = -0.2
        #       self.publisher_3.publish(myTwist)
          except Exception as e:
            self.get_logger().error('Error getting waypoint: {}'.format(e))
        else:
          color = (0, 0, 255)
        # frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
  
#   def camInfo_callback(self, msg):
#     print("Camera Info Message: ", msg)
#     self.K = np.array(msg.k).reshape(3, 3)
#     self.R = np.array(msg.r).reshape(3, 3)
#     P = np.reshape(msg.p, (3, 4))
#     # print("Value of P: ", P)
#     Tx = -P[0][3] / P[0][0]
#     Ty = -P[1][3] / P[1][1]
#     Tz = -P[2][3] / P[2][0]
#     T1 = [Tx, Ty, Tz]
#     print("T1: ", T1)
#     # self.t = np.array([Tx, Ty, Tz])
#     K_inv = np.linalg.inv(self.K)
#     T = K_inv.dot(P[:, 3])
#     print("Value of T: ", T)
#     self.t = T
 
#     # Display the message on the console
#     self.get_logger().info('Publishing video frame')

#   def depth_callback(self, msg):
#     try:
#         self.depthMap = self.br.imgmsg_to_cv2(msg, "passthrough")
#         print("Depth Map Type", type(self.depthMap))
#         print("Depth Map Shape", self.depthMap.shape)
#     except Exception as e:
#         self.get_logger().error('Error converting ROS Image to DepthMap: {}'.format(e))
#         return
  
#   def getFollowString_callback(self, msg):
#     self.toFollowString = msg.data
  
#   def timer_callback(self):
#     depthofPoint = self.depthMap[self.midpoint[0], self.midpoint[1]]
#     myWaypoint = (self.midpoint[0], self.midpoint[1], depthofPoint)

  
def main(args=None):
  
  # Initialize the rclpy library
  rclpy.init(args=args)
  
  # Create the node
  image_publisher = ImagePublisher()
  
  # Spin the node so the callback function is called.
  rclpy.spin(image_publisher)
  
  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  image_publisher.destroy_node()
  
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()