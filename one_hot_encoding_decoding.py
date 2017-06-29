__author__ = 'Sejune Cheon'

## used Python 3.5

## Y 값을 one hot encoding 또는 decoding 하기


## import library

import numpy as np
import keras

## read data
dataY = np.load("data_sample/numpy/data_Y.npy")

## one-hot encoding
encoded_Y = keras.utils.to_categorical(dataY, 4) #(변환할 데이터, class 종류 개수)

## one-hot decoding
decoded_Y = np.argmax(encoded_Y, axis=1) # (변환할 데이터, argmax 기준 축)
# 축에 대한 지정은 encoded_Y.shape을 해보면 데이터의 차원수가 출력되는데 여기서 기준으로 잡고 싶은 축을 정하면 된다.
# shape 카운트도 0부터 시작

