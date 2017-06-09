__author__ = 'Sejune Cheon'

# two ways of reading and opening image data

# first way is to use opencv
# opencv reads the RGB image in BGR order and when use the opencv viewer for viewing images

import cv2
import matplotlib.pyplot as plt

data_path = "data_sample/000001.jpg"

img = cv2.imread(data_path)  #image is read as BGR

cv2.namedWindow("", cv2.WINDOW_NORMAL) # makes the window resizable, if it is commented the image viewer window will not be resizable
cv2.imshow("", img) # it shows image in BGR so the image is properly viewed
cv2.waitKey() # holds the window


# to convert the BGR image to RGB.
img_converted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("", img_converted) # cv2.imshow is a BGR viewer so the converted RGB image will be viewed odd
cv2.waitKey()

# need to use RGB viewer like as matplotlib's plt.imshow()
plt.imshow(img_converted)
plt.axis("off")
plt.show()



# second way is to use matplotlib

img_rgb = plt.imread(data_path) # RGB image reader

plt.imshow(img_rgb) # RGB image viewr



## I think it is not working properly ##
## cv2 color value range setting
# 0 to 255 for CV_8S images
# 0 to 65535 for CV_16S images
# 0 to 1 for CV_32F images

# img8 = cv2.cvtColor(img_rgb, cv2.CV_8S)
# img16 = cv2.cvtColor(cv2.cvtColor(img_rgb, cv2.CV_16S), cv2.COLOR_BGR2RGB)
# img_32f = cv2.cvtColor(img_converted, cv2.CV_32SC4)