#   OpenCv Setup and Hello World programs in Python and C++
made by Lucas Schmirl 20.02.2022, info.hellgineer@gmail.com, last edit: 24.02.2022

<br>

# Virtual environment installation (optional)

For using openCv inside a virtual environment install a `venv`:

Inside this `venv`, packages can be installed (e.g. `pip`) which are only accessible inside this `venv` (not system wide). If you delete the `venv`, all containing packages are deleted.

if not needed, skip to [OpenCv for Python](#opencv-installation-for-use-with-python) or [OpenCv for C++](#opencv-installation-for-use-with-c)

otherwise create a folder for your project:
```bash
mkdir openCv
```
And install `venv`:

```bash
sudo apt install -y python3-venv
```

To create an virtual environment (usage: `python3 -m venv <name-of-your-venv>`)

```bash
python3 -m venv .venv
```
(hiding the folder is optional)

<br>

To activate the environment (usage: `source <name-of-your-venv>/bin/activate`)
```bash
source .venv/bin/activate
```

To deactivate the environment:
```bash
deactivate
```

<br>


# If you want to use PYTHON:

(if not interested in python, skip to [the REAL language](#if-you-want-to-use-c) lol)

## OpenCv installation for use with Python

If not already done, create a folder for the project:
```bash
mkdir openCv
```

For use with Python continue by installing the openCv pip package.

If you want to install only inside `venv`, first enter it using: 
```bash
source <name-of-your-venv>/bin/activate
```
and then do:
```bash
pip install opencv-contrib-python
```

or install specific version, usage: `pip install opencv-contrib-python==<version>`

```bash
pip install opencv-contrib-python==3.4.0
```

This will fail because there is no `3.4.0`.

From the error message you can now choose your beloved version and re-run the last command with chosen version.

Now your openCv installation for python is complete.

You can test the version of the opencv installation by running `openCv_version.py`.

<br>
<br>


### Content: 
`requirements.txt` (lists all needed pkg's)

`scripts/openCv_version.py` (displays currently used openCv version)

`scripts/helloworld.py` (python script to load and display image)

`scripts/getcam.py`   (python script to show accessible webcam)

`scripts/take_pic.py`   (python script to take image from webcam)

`PICs/Schaukelbub.png` (image source)

<br>

### USAGE: 
```bash
python3 scripts/openCv_version.py
python3 scripts/hello_world.py
python3 scripts/take_pic.py
python3 scripts/getcam.py
```
### To setup your pkg on other machines:
```bash
pip install -r requirements.txt
```

<br>
<br>


# If you want to use C++:

## OpenCv installation for use with C++

For use with C++ continue by installing openCv system-wide.

To get root rights (because you are going to mess around in `/opt`):
```bash
sudo -s
```

Change dir to `/opt`:
```bash
cd /opt
```

If you installed the wrong version or have another version installed already, first [uninstall the old version](#uninstall-an-old-opencv-version-c)

<br>

Get `opencv 3.4.13` and `opencv_contrib 3.4.13` (***The Moodle Version***):
```bash
wget -O opencv.zip https://github.com/opencv/opencv/archive/refs/tags/3.4.13.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/refs/tags/3.4.13.zip
```


Unzip both:
```bash
unzip opencv.zip
unzip opencv_contrib.zip
```

Change the name of these two folders:
```bash
mv opencv-3.4.13 opencv
mv opencv_contrib-3.4.13 opencv_contrib
```

To build, run the following commands line by line (thaks to [Fynn](https://github.com/fynnbehnke) its so easy): 
```bash
cd opencv
mkdir release
cd release

cmake -D BUILD_TIFF=ON -D WITH_CUDA=OFF -D ENABLE_AVX=OFF -D WITH_OPENGL=OFF -D WITH_OPENCL=OFF -D WITH_IPP=OFF -D WITH_TBB=ON -D BUILD_TBB=ON -D WITH_EIGEN=OFF -D WITH_V4L=OFF -D WITH_VTK=OFF -D BUILD_TESTS=OFF -D BUILD_PERF_TESTS=OFF -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_EXTRA_MODULES_PATH=/opt/opencv_contrib/modules /opt/opencv/

make -j4
make install
ldconfig

exit
cd
```
Finally, version `3.4.13` is installed (for C++).

Now move to the folder where you cloned this repo to.

Or to the folder where you have your own source files.

You can check the version of your opencv installation using [build](#build) and [check-version](#check-for-version)

<br>
<br>


### Content: 
`Makefile` (to build the project, compiling and linking)

`src/main.cpp` (source file)

`src/openCv_version.cpp` (displays currently used openCv version)

`PICs/Schaukelbub.png` (image source)

<br>


### Build:
```bash
make
```

### Check for version:
```bash
./checkVersion
```

### Usage of helloWorld: 
```bash
./helloWorld <path-to-image>
```

<br>
<br>
<br>

# Additional information

<br>

## System used
- WSL2 version: 1.0.3.0 on Win11
- Ubuntu 20.04.5 LTS
- Python version: 3.8.10
- opencv-contrib version: 4.7.0.68 (for Python)
- opencv-contrib version: 3.4.13 (for C++)


<br>

## Uninstall an old opencv version (C++)
If you have a wrong version already installed you can `cd` into the folder where you did `make install` the last time and:
```bash
cd opencv/release
make uninstall
```
after this, the previously installed version is uninstalled. Then install the [new version](#opencv-installation-for-use-with-c)

<br>

<br>

## Weird WSL bugs

### When using older versions of WSL2 the Image-Windows close immediately or don't close at all after using the keyboard to interact with `waitkey(0)` because the key chache can get stuck. 


Workaround is to **restart your WSL** from `PowerShell` using:
```powershell
wsl --shutdown
```
Fix (that worked for me) is to simply update your WSL from `PowerShell` using:

```powershell
wsl --update
```

Update your stuff inside WSL from `bash` using:
```bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt update && sudo apt upgrade -y
```

<br>

### `Error: Package OpenCV or file opencv.pc not found` when using `make`
check for PATH:

https://prateekvjoshi.com/2013/10/18/package-opencv-not-found-lets-find-it/

<br>

### PYTHON-WEBCAM HUSTLE ONLY!

Accessing USB-DEVICES is not possible using WSL2 without building your own kernel.

- Video for kernel rebuild:

    https://www.youtube.com/watch?v=t_YnACEPmrM

- corresponding commands to video:
    
    https://agiledevart.github.io/wsl2_usb_camera.txt
    
- Kernel:
    
    https://github.com/microsoft/WSL2-Linux-Kernel/releases/tag/linux-msft-wsl-5.15.79.1

- (Advice on cam&mic in WSL2):

    https://version-2.com/zh/2022/02/advice-on-camera-and-microphone-in-wsl2-ubuntu/

### REBUILDING THE KERNEL TO SPICY FOR ME - good luck

