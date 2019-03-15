# phobos-ros
ROS driver for I3Dr's Phobos stereo camera.

Phobos is a high resolution (5MP), high accuracy (sub-mm up to a few metres), global shutter stereo imaging system . This ROS package aims to be a starting point to developing ROS-based applications with Phobos. The package uses `gscam` as the camera driver and provides:

* Adjustment of frame sizes
* Adjustment of frame rate (currently up to 30 fps at 5MP)

Camera properties (i.e. Exposure, Gain) can be controlled using services after launching the tiscamera_ctrl node
This is detailed in the example launch file 'phobos.launch'.

Stereo calibration of Phobos can be done using the launch files provided.

Package includes support for hand-eye calibration through alvar markers.

Support will soon be added for control over triggering.