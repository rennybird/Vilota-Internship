# Install Dependencies
## Install lib
sudo apt-get install liblapack-dev libsuitesparse-dev libmetis-dev libgflags-dev libgoogle-glog-dev


## Install Ceres 
git clone https://github.com/urbste/pyTheiaSfM
cd pyTheiaSfM  
mkdir -p build && cd build
cmake .. 
make -j
sudo make install

## Install  TheiaSfM fork
git clone https://github.com/urbste/pyTheiaSfM
mkdir -p build && cd build 
cmake..
make -j

## Build Project
git clone https://github.com/urbste/OpenImuCameraCalibrator
mkdir -p build && cd build && cmake ..
cmake..
make -j


# Change path to my own directory
    from
    parser.add_argument('--path_to_build', 
                        help="Path to OpenCameraCalibrator build folder.",
                        default='/home/steffen/projects/OpenImuCameraCalibrator/build/applications') 
    to
    parser.add_argument('--path_to_build', 
                        help="Path to OpenCameraCalibrator build folder.",
                        default='/home/renny/work/Vilota/Problem Solving/OpenImuCameraCalibrator/build/applications') 

## I also need to change some line due to my python environment need to called with python3 command
bias_estimation = Popen(["python", py_imu_file,
to
bias_estimation = Popen(["python3", py_imu_file,


# Run
python3 python/run_gopro_calibration.py --path_calib_dataset=MyDataset --checker_size_m=0.021 --image_downsample_factor=2 --camera_model=DIVISION_UNDISTORTION
I change to --path_calib_dataset=MyDataset because it's where my dataset is

# Question
a.Camera model used for calibrating the camera
Ans. DIVISION_UNDISTORTION

b.Camera intrinsic values
Ans.    Aspect Ratio: 0.9976160980286715
        Division Undistortion Distortion: -1.418929254561896e-06
        Focal Length: 437.9181337088973
        Principal Point X: 480.8251065016253
        Principal Point Y: 273.75058536535875
        Skew:: 0.0

c.Extrinsic between IMU and camera (T_camera_to_imu)
Ans.    Rotation QIC
        w: 0.0008431393548534723
        x: -0.00321466546909513
        y: -0.7086821448257915
        z: 0.7055200724621987
        Translation TIC
        x: 0.00418488776745489
        y: -0.025570270212293453
        z: 0.0037432912916619482

d.Time offset IMU to camera
Ans.    -0.012422480060567525