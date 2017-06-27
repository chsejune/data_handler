__author__ = 'Sejune Cheon'

## tested on Python3

# import libraries
import matplotlib.pyplot as plt
import cv2

# sample data path
data_path = "data_sample/images/000001.jpg"

## read image
img_rgb = plt.imread(data_path)


## resize image
resized_img = cv2.resize(img_rgb, (89, 109))  #(src=image_to_resize, dsize=(width, height), interpolation=cv2.INTER_LINEAR)

"""
src – input image.
dsize – output image size
interpolation – interpolation method:
INTER_NEAREST - a nearest-neighbor interpolation
INTER_LINEAR - a bilinear interpolation (used by default)
INTER_AREA - resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire’-free results. 
             But when the image is zoomed, it is similar to the INTER_NEAREST method.
INTER_CUBIC - a bicubic interpolation over 4x4 pixel neighborhood
INTER_LANCZOS4 - a Lanczos interpolation over 8x8 pixel neighborhood
To shrink an image, it will generally look best with CV_INTER_AREA interpolation, 
whereas to enlarge an image, it will generally look best with CV_INTER_CUBIC (slow) or CV_INTER_LINEAR (faster but still looks OK).
"""

