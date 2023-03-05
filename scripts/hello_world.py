#	made by Lucas Schmirl 20.02.2022,	last edit: 20.02.2022

import cv2
# https://www.youtube.com/watch?v=qCR2Weh64h4

pathToPic = '/home/lucas/MSC/MVSR/openCv/PICs/Schaukelbub.png'


## FUNCTIONS
def clean_up():
    cv2.waitKey(0) # wait infinite [s], pressing key moves to next line (during given time) after time moves to next line automatically
    cv2.destroyAllWindows()

# save Image
def save_picture_as(name, img):
   cv2.imshow(f'picture to be saved as {name}', img)
   cv2.imwrite(name, img)

def get_info_of_img(img):
    # show Image-type, shape and color values.          #openCv (RGB) is (BGR)
    print(f'\nImage type is:\t{type(img)}')
    print(f'Array shape is:\t{img.shape}') # array: (rows, columns, channels) == (height, width, color space)
    print(f'\nColor values at specific area:\n {img[120][150:200]}') # get color values of row 120 and width in range of 150-200



if __name__ == '__main__':

    # load Image
    img_color = cv2.imread(pathToPic, cv2.IMREAD_COLOR) # cv2.IMREAD_COLOR expands to -1, cv2.IMREAD_GRAYSCALE (0), cv2.IMREAD_UNCHANGED (1)
    # img_grayScale = cv2.imread(pathToPic, 0)
    # img_unchanged = cv2.imread(pathToPic, 1)

    # get info of Image
    # get_info_of_img(img_color)

    # resize Image
    #img_color = cv2.resize(img_color, (400,400))
    #img_color = cv2.resize(img_color, (0,0), fx=0.5, fy=0.5)

    # rotate Image
    # img_rot = cv2.rotate(img_color, cv2.ROTATE_90_CLOCKWISE)

    # save Image
    # save_picture_as('PICs/new_img.png', img_rot)

    # show Image
    cv2.imshow('Color-Image: Schaukelbub', img_color)
    # cv2.imshow('GrayScale-Image: Schaukelbub', img_grayScale)
    # cv2.imshow('Unchanged-Image: Schaukelbub', img_unchanged)


    clean_up()








