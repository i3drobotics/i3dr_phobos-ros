from Stereo3D import Stereo3D, StereoCapture, StereoCalibration

camera_name = "phobos"
stcap = StereoCapture("Phobos",["22864917","22864912"])

# define inout folder
folder = "cal/"

stcap.runGui(folder,False)