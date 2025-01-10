#!/bin/bash
# SPDX-FileCopyrightText: 2025 Hiroaki Ohmatsu
# SPDX-License-Identifier: BSD-3-Clause



dir=~
[ "$1" != "" ] && dir="$1"  


cd $dir/ros2_ws
colcon build
source $dir/.bashrc


timeout 20 ros2 run batterynode battery &


sleep 2


timeout 10 ros2 topic echo /battery_info > /tmp/batterynode.log


if grep -q "バッテリー残量" /tmp/batterynode.log; then
    
    cat /tmp/batterynode.log | grep 'バッテリー残量'


fi

