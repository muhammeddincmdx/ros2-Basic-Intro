#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("python_test")
        self.counter_ =0
        self.get_logger().info("OOP Node")
        self.create_timer(0.5,self.timer_callback) # "1/0.5= 2 times one second"
        
    def timer_callback(self):
        self.counter_+=1
        if self.counter_ ==1:
            self.get_logger().info(f"it has been {self.counter_} day.")
        else:
            self.get_logger().info(f"it has been {self.counter_} days.")


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    """
    # old version
    node = Node("python_test")
    node.get_logger().info("hello_ros_2_:|")
    """
    rclpy.spin(node)
    rclpy.shutdown

if __name__==  "__main__":
    main()