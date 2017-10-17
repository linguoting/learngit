# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
##样本数据(Xi,Yi)，需要转换成数组(列表)形式
Xi=np.array([50,52,52,54,56,58,61,64,67,70]) #身高
Yi=np.array([50,52,52,54,56,58,61,64,67,70])#体重
#画样本点
plt.figure(figsize=(8,6)) ##指定图像比例： 8：6
plt.scatter(Xi,Yi,color="green",label="样本数据",linewidth=3) 
plt.show()

