#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 run mypkg battery & sleep 5

timeout 10 ros2 topic echo /battery > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'data: 96'
