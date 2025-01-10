# SPDX-FileCopyrightText: 2025 Hiroaki Ohmatsu
# SPDX-License-Identifier: BSD-3-Clause


import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class BatteryNode(Node):

    def __init__(self):
        super().__init__('battery')
        
        self.publisher_ = self.create_publisher(String, 'battery_info', 10)  
        
        self.timer = self.create_timer(2.0, self.publish_battery_info)  

        self.get_logger().set_level(rclpy.logging.LoggingSeverity.WARN)
        
        self.declare_parameter('battery_warning_threshold', 20)
    
    def publish_battery_info(self):
        battery = psutil.sensors_battery()
        if battery:
            battery_info = f"バッテリー残量: {battery.percent}% | 電源接続中: {'はい' if battery.power_plugged else 'いいえ'}"
            if not battery.power_plugged:
                battery_info += f" | 残り時間: {battery.secsleft // 60}分"
        
            battery_warning_threshold = self.get_parameter('battery_warning_threshold').value
            if battery.percent < battery_warning_threshold:
                battery_info += f" | 警告: バッテリー残量が{battery_warning_threshold}%を下回りました！"



        else:
            battery_info = "バッテリー情報は取得できません。"
        
        
        msg = String()
        msg.data = battery_info
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published: {battery_info}")


def main():
    rclpy.init()
    node = BatteryNode()  
    rclpy.spin(node)  

if __name__ == '__main__':
    main()

