__author__ = 'Sejune Cheon'

# developed and tested on python3

## 클래스별로 분류되어 있는 이미지 데이터를 불러들여, 클래스 정보와 함께 이미지 데이터를 numpy 형태로 저장
## 동시에 이미지 resize 작업도 진행

## for this example we assume that the size of images(width and height) are all the same.

# import libraries
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

## 불러올 데이터 폴더, 이하 폴더에 클래스 레이블 별로 폴더가 정리되어 있음
image_path = r"data_sample\images"
image_dir = os.listdir(image_path)

## 데이터에 클래스 레이블 정보 부여와 함께 numpy 행렬로 저장하기
class_num=0 # 0부터 순차적으로 클래스를 부여하기 위해 클래스 변수 초기화
image_set_Y=[]  # 불러드린 이미지의 클래스 레이블들 저장 변수
image_set_X=[]  # 불러드린 이미지들 저장 변수
for d in image_dir:
    file_list = os.listdir(os.path.join(image_path,d))  # 해당 path에 속한 file list 읽어오기
    for f in file_list:
        image = plt.imread(os.path.join(image_path,d,f))  # 이미지 읽기
        resized_img = cv2.resize(image, (89, 109))  # 이미지 resize / (width, height)
        image_set_X.append(resized_img)  # 불러들인 이미지 리스트에 저장
        image_set_Y.append(class_num)   # 불러들인 이미지의 클래스 레이블 정보 리스트에 저장
    class_num+=1

# numpy array 로 이미지 데이터와 이미지 클래스 레이블 정보를 저장
np.save("datasets/resized_img_180x120_X.npy", np.array(image_set_X))
np.save("datasets/resized_img_180x120_Y.npy", np.array(image_set_Y))




# for img in image_set_X:
#     print(img.shape)
