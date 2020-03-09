from Stereo3D import Stereo3D, StereoCapture, StereoCalibration

# define inout folder
folder = "cal2/"

# define calibration directories
left_images_folder = folder
right_images_folder = folder
output_folder = folder
left_wildcard = "*_l.png"
right_wildcard = "*_r.png"
grid_size = 39.0
grid_rows = 6
grid_cols = 8
# generate calibration from images
stcal = StereoCalibration()
stcal.calibrate(
    left_images_folder,right_images_folder,
    output_folder,left_wildcard,right_wildcard,
    grid_size, grid_rows, grid_cols
)