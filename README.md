# phobos-ros
ROS driver for I3Dr's Phobos stereo camera.

Phobos is a high resolution (5MP), high accuracy (sub-mm up to a few metres), global shutter stereo imaging system . This ROS package aims to be a starting point to developing ROS-based applications with Phobos. The package uses `gscam` as the camera driver and provides:

* Adjustment of frame sizes
* Adjustment of frame rate (currently up to 30 fps at 5MP)

Support will soon be added for control over triggering.
