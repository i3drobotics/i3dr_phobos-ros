# I3DR Phobos ROS

ROS driver for I3Dr's Phobos stereo camera.

Phobos is a high resolution (5MP), high accuracy (sub-mm up to a few metres), global shutter stereo imaging system . This ROS package aims to be a starting point to developing ROS-based applications with Phobos. 

This package will work with both Basler and The Imaging Source implimentations of the Phobos Stereo Systems.
Basler implimentation will work as USB or GigE. 

## Requirements

This package relies on the **i3dr_stereo_camera** package for capture and generation of 3D. Please make sure you have the **i3dr_stereo_camera** package in your workspace.
[link](https://github.com/i3drobotics/i3dr_stereo_camera-ros.git)

## Calibration
Python scripts are provided for calibration outside of ros. 
Capture images from Phobos camera using capture.py
Then calibrate the captured images using calibrate.py
An example calibration is provided in 'cal'
