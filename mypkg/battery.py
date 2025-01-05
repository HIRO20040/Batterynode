# SPDX-FileCopyrightText: 2025 Hiroaki Ohmatsu
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


rclpy.init()
node = Node("battery")
pub = node.create_publisher(Int16, "battery", 10)
n = 100



def cb():
    global n
    msg = Int16()
    msg.data = n
    pub.publish(msg)
    n -= 1

def main():
        node.create_timer(1.0, cb)
        rclpy.spin(node)

if __name__ == '__main__':
    main()

