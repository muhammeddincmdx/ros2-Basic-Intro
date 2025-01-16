
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

"""
to use String we add this library after the add we update package.xml
<depend> example_interfaces.msg</depend>
also to take information about String 
use this code in terminal 
$ros2 interface show example_interfaces/msg/String 
# This is an example message of using a primitive datatype, string.
# If you want to test with this that's fine, but if you are deploying
# it into a system you should create a semantically meaningful message type.
# If you want to embed it in another message, use the primitive data type instead.
string data

"""

class RobotStatePublisherNude(Node):
    def __init__(self):
        super().__init__("robot_state_publisher") 
        self.robot_name = "WALL-E"
        #to create publisher
        self.publisher_=self.create_publisher(msg_type=String,topic="state_publisher",qos_profile=10)
        #create_publisher(message_type= "it could be new type or defatult ros2 types",topic="name of topic",qos_profile= buffer size)

        self.timer=self.create_timer(timer_period_sec=0.5,callback=self.publish_state)
        self.get_logger().info(message="Robot state publisher has started.")
        # to check code is working properly

    def publish_state(self):
        msg=String() #String data
        msg.data=F"This is {self.robot_name} from PIXAR"
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotStatePublisherNude() 

    rclpy.spin(node)
    rclpy.shutdown

if __name__==  "__main__":
    main()




