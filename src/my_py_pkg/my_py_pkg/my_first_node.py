#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node = Node("py_test1")
    node.get_logger().info("Hello ROS2 First")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()