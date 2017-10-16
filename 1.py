# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

##样本数据(Xi,Yi)，需要转换成数组(列表)形式
Xi=np.array([152,156,160,164,168,172,176,180,184,188])
Yi=np.array([50,52,52,54,56,58,61,64,67,70])

##需要拟合的函数func :指定函数的形状 
def func(p,x):
    k,b=p
    return k*x+b

##偏差函数：x,y都是列表:这里的x,y更上面的Xi,Yi中是一一对应的
def error(p,x,y):
    return func(p,x)-y

#k,b的初始值，可以任意设定,经过几次试验，发现p0的值会影响cost的值：Para[1]
p0=[1,20]

#把error函数中除了p0以外的参数打包到args中(使用要求)
Para=leastsq(error,p0,args=(Xi,Yi))

#读取结果
k,b=Para[0]
print("k=",k,"b=",b)


#画样本点
plt.figure(figsize=(8,6)) ##指定图像比例： 8：6
plt.scatter(Xi,Yi,color="green",label="sample-data",linewidth=2) 

#画拟合直线
x=np.linspace(150,190,100) ##在150-190直接画100个连续点
y=k*x+b ##函数式
plt.plot(x,y,color="red",label="fitted-line",linewidth=2) 
plt.legend() #绘制图例
plt.show()
