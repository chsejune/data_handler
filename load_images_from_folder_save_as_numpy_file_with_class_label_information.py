__author__ = 'Sejune Cheon'

# developed and tested on python3

## for this example we assume that the size of images(width and height) are all the same.

# import libraries
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

image_path = r"D:\Data_Samples\eye_data\fundus_photo_sample_600"
image_dir = os.listdir(image_path)

class_num=0
image_set_Y=[]
image_set_X=[]
for d in image_dir:
    file_list = os.listdir(os.path.join(image_path,d))
    for f in file_list:
        image = plt.imread(os.path.join(image_path,d,f))
        resized_img = cv2.resize(image, (180, 120))
        image_set_X.append(resized_img)
        image_set_Y.append(class_num)
    class_num+=1

np.save("datasets/resized_img_180x120_X.npy", np.array(image_set_X))
np.save("datasets/resized_img_180x120_Y.npy", np.array(image_set_Y))


# for img in image_set_X:
#     print(img.shape)
