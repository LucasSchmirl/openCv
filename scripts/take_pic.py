#	made by Lucas Schmirl 20.02.2022,	last edit: 20.02.2022

import cv2
import time

# need to add/export cam to WSL to make it accessible
# from powershell with admin rights do
# usbipd wsl list # and get BUSID from Camera
# usbipd wsl attach --busid x-y # attaching camera to ubuntu
# then in WSL check for video using: ls /dev/bus/usb
# also try lsusb
# currently not working




## ACESSING USB-DEVICES IS NOT POSSIBLE USING WSL2 WITHOUT BUILDING YOUR OWN KERNEL

# (Advice on cam&mic in WSL2) ## https://version-2.com/zh/2022/02/advice-on-camera-and-microphone-in-wsl2-ubuntu/

# Video for kernel rebuild    ## https://www.youtube.com/watch?v=t_YnACEPmrM
# commands                    ## https://agiledevart.github.io/wsl2_usb_camera.txt
# Kernel                      ## https://github.com/microsoft/WSL2-Linux-Kernel/releases/tag/linux-msft-wsl-5.15.79.1

## THIS IS TO SPICY FOR ME!!

## Camera Data
videoDevice = 0  #webcam
camResolution_width = 640       #picture width  [px]    #800   640   320   160
camResolution_height = 480      #picture height [px]    #600   480   240   120


##FUNCTIONS
def make_and_convert_pic():     #take webcam picture and convert it to RGB
   cam = cv2.VideoCapture(videoDevice, cv2.CAP_V4L2)
   #cam = cv2.VideoCapture(cv2.CAP_V4L2)
   time.sleep(0.1)
   cam.set(3, camResolution_width)                                      
   cam.set(4, camResolution_height)
   img = cam.read()[1]
   cam.release()
   return img #cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# save Image
def save_picture_as(name, img):
   cv2.imshow(f'picture to be saved as {name}', img)
   cv2.imwrite(name, img)

def clean_up():                                                         #wait for cam and free it afterwards
    cv2.waitKey(0) # wait infinite [s], pressing key moves to next line (during given time) after time moves to next line automatically
    cv2.destroyAllWindows() # better close with ctrl + z on WSL : https://stackoverflow.com/questions/69379095/python-opencv2-imshow-is-closing-immediately-even-with-waitkey0




if __name__ == '__main__':

    # capture Image with cam
    snapshot = make_and_convert_pic()
    save_picture_as('PICs/snapshot.png', snapshot)

    clean_up()