# I3DR Phobos ROS

ROS driver for I3DR's Phobos stereo camera.

Phobos is a high resolution (5MP), high accuracy (sub-mm up to a few metres), global shutter stereo imaging system . This ROS package aims to be a starting point to developing ROS-based applications with Phobos. 

This package will work with both Basler and The Imaging Source implimentations of the Phobos Stereo Systems.
Basler implimentation will work as USB or GigE. 

## Status
![ROS Build](https://github.com/i3drobotics/i3dr_phobos-ros/workflows/ROS%20Build/badge.svg?event=push)

## Installation

For an easy setup, a rosinstall file is provided in 'install' folder of this repo which can be used to get this package and it's dependent ros packages in your workspace. 
In your ROS workspace use the following command:
```
wstool init src https://raw.githubusercontent.com/i3drobotics/i3dr_phobos-ros/master/install/i3dr_phobos_https.rosinstall
```
If you already have a wstool workspace setup then use the following command instead:
```
wstool merge -t src https://raw.githubusercontent.com/i3drobotics/i3dr_phobos-ros/master/install/i3dr_phobos_https.rosinstall
wstool update -t src
```

If you do not use wstool, you can download the packages using the following command:
```
cd PATH_TO_ROS_WS/src
git clone https://github.com/i3drobotics/i3dr_phobos-ros.git
git clone https://github.com/i3drobotics/i3dr_stereo_camera-ros.git
git clone https://github.com/i3drobotics/camera_control_msgs.git
git clone https://github.com/i3drobotics/pylon_camera.git
git clone https://github.com/i3drobotics/i3dr_rosserial_phobos-ros.git
```

To install package dependences use rodep:
```
rosdep install --from-paths src --ignore-src -r -y
```

Build using catkin (tested with catkin_make and catkin_build):
```
catkin_make
or
catkin build
```

Plug in your Phobos camera to your machine and use the following launch file to test:
```
roslaunch i3dr_phobos phobos.launch
```

To check everything is working add the paramter 'rviz':
```
roslaunch i3dr_phobos phobos.launch rviz:=true
```
