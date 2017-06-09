__author__ = 'Sejune Cheon'

# tested in python 3.5

# two ways of reading and opening image data (some image conversion methods included)

# first way is to use opencv
# opencv reads and views the RGB image in BGR order.


# importing libraries
import cv2 # in color image, BGR is used as default
import matplotlib.pyplot as plt # in color image RGB is used as default
import skimage as ski # in color image RGB is used as default

# sample data path
data_path = "data_sample/000001.jpg"

img = cv2.imread(data_path)  #image is read in BGR

cv2.namedWindow("", cv2.WINDOW_NORMAL) # makes the window resizable, if it is commented the image viewer window will not be resizable
cv2.imshow("", img) # it shows image in BGR so the image is properly viewed
cv2.waitKey() # holds the window

# to convert the BGR image to RGB.
img_converted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("", img_converted) # cv2.imshow is a BGR viewer so the converted RGB image will be viewed odd
cv2.waitKey()

# now to view image, need to use RGB viewer like as matplotlib's plt.imshow()
plt.imshow(img_converted)
plt.axis("off")
plt.show()


# second way is to use matplotlib for read image and view image

img_rgb = plt.imread(data_path) # RGB image reader (for datatype: read png image as float32, others reads as uint8)

plt.imshow(img_rgb) # RGB image viewer



# convert image data types
# Data type	  Range
# uint8	      0 to 255
# uint16	  0 to 65535
# uint32	  0 to 232
# float	     -1 to 1 or 0 to 1
# int8	     -128 to 127
# int16	     -32768 to 32767
# int32	     -231 to 231 - 1

# use skimage for converting image data types

# from uint8 to float (vise versa)
img = plt.imread(data_path)
imgf = ski.img_as_float(img) # img_as_float: Convert to 64-bit floating point.
img8 = ski.img_as_ubyte(imgf) # img_as_ubyte: Convert to 8-bit uint.





## I think it is not working properly ##
## cv2 color value range setting
# 0 to 255 for CV_8S images
# 0 to 65535 for CV_16S images
# 0 to 1 for CV_32F images

# img8 = cv2.cvtColor(img_rgb, cv2.CV_8S)
# img16 = cv2.cvtColor(cv2.cvtColor(img_rgb, cv2.CV_16S), cv2.COLOR_BGR2RGB)
# img_32f = cv2.cvtColor(img_converted, cv2.CV_32SC4)