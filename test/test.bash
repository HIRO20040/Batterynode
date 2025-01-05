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


timeout 10 ros2 topic echo /battery > /tmp/batterynode.log 

if grep -q "data:" /tmp/batterynode.log; then
    cat /tmp/batterynode.log | grep '91'
else
    echo "data: not found"
fi
