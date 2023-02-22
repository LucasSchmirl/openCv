#   OpenCv Setup and Hello World programs in python and C++
made by Lucas Schmirl 20.02.2022, info.hellgineer@gmail.com, last edit: 21.02.2022

<br>

# General:

## Virtual environment installation

For using openCv inside a virtual environment install a `venv` (virtual environment):

Inside this `venv`, packages can be installed (f.e. `pip`) which are only accessible inside this `venv` (not system wide). If you delete the `venv`, all containing packages are deleted.

if not needed, skip to [OpenCv installation](#opencv-installation)

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

## OpenCv installation

If not already done create a folder for the project:
```bash
mkdir openCv
```

Continue by installing the openCv pip package:
```bash
pip install opencv-contrib-python
```

or install specific version, usage: `pip install opencv-contrib-python==<version>`

```bash
pip install opencv-contrib-python==3.4.0
```

If error: repeat the command with available version shown in terminal

If this install fails, check out your versions with:
```bash
pip --version
python --version
```
and check the internet to find out which versions are the minimal requirement. 

Maybe you just need to upgrade your stuff using.

```bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt update && sudo apt upgrade -y
```

And/Or [restart your WSL](#weird-wsl-bugs)

<br>
<br>

# If you want to use PYTHON:

if not interested in python, skip to [the REAL language](#if-you-want-to-use-c)

### Content: 
`requirements.txt` (lists all needed pkg's)

`scripts/helloworld.py` (python script to load and display image)

`scripts/getcam.py`   (python script to show accessible webcam)

`scripts/take_pic.py`   (python script to take image from webcam)

`PICs/Schaukelbub.png` (image source)

<br>

### USAGE: 
```bash
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

### Content: 
`Makefile` (to build the project, compiling and linking)

`src/main.cpp` (source file)

`PICs/Schaukelbub.png` (image source)

<br>

### Install Librarys:
```bash
sudo apt-get install -y libopencv-dev
```

### Build:
```bash
make
```
### Usage: 
```bash
./helloWorld <path-to-image>
```

<br>
<br>
<br>

## Additional information

<br>

### System used
- WSL2 version: 1.0.3.0 on Win11
- Ubuntu 20.04.5 LTS
- Python version: 3.8.10
- opencv-contrib version: 4.7.0.68


<br>

### Weird WSL bugs

- When using older version of WSL2 pics close immideately or dont close at all after using the keyboard to interact with `waitkey(0)` the key chache can get stuck. 

    Workaround is to **restart your WSL** from `PowerShell` using:
    ```powershell
    wsl --shutdown
    ```
    Fix that worked for me is to simply update your WSL from `PowerShell` using:

    ```powershell
    wsl --update
    ```

<br>

- `Error: Package OpenCV or file opencv.pc not found` when using `make`
    check for PATH:
    https://prateekvjoshi.com/2013/10/18/package-opencv-not-found-lets-find-it/

<br>

- PYTHON-WEBCAM HUSTLE ONLY!

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
