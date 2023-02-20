#	made by Lucas Schmirl 20.02.2022,	last edit: 20.02.2022

import cv2
import time

# need to add/export cam to WSL to make it accessible
# from powershell with admin rights do
# usbipd wsl list # and get BUSID from Camera
# usbipd wsl attach --busid x-y # attaching camera to ubuntu
# then in WSL check for video using: ls /dev/bus/usb
# currently not working

## Camera Data
videoDevice = 1 # webcam
camResolution_width = 640       #picture width  [px]    #800   640   320   160
camResolution_height = 480      #picture height [px]    #600   480   240   120


##FUNCTIONS
def make_and_convert_pic():     #take webcam picture and convert it to RGB
   cam = cv2.VideoCapture(videoDevice, cv2.CAP_DSHOW)
   time.sleep(0.1)
   cam.set(3, camResolution_width)                                      
   cam.set(4, camResolution_height)
   img = cam.read()[1]
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