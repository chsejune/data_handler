__author__ = 'Sejune Cheon'

# python 3.5 used

import scipy.stats as ss
import numpy as np

## class label 별 개수를 count 한다.

dataY = np.load("data_sample/numpy/data_Y.npy") # numpy 를 이용하여 저장되어 있던 numpy array를 불러들인다.

print(ss.itemfreq(dataY)) # 각 클래스별 데이터 개수 출력

