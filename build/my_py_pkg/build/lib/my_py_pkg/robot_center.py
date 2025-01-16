
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotCenterNode(Node):
    def __init__(self):
        super().__init__("robot_center") 
        self.subscriber_=self.create_subscription(msg_type=String,topic="state_publisher",callback=self.callback_center,qos_profile=10)
        #self.create_subscription(msg_type,topic,callback,buffer frame)
        self.get_logger().info("Robot center is operating")
        

    def callback_center(self,msg):
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = RobotCenterNode() 

    rclpy.spin(node)
    rclpy.shutdown

if __name__==  "__main__":
    main()