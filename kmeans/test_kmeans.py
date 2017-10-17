from numpy import *  
import time  
import matplotlib.pyplot as plt  
import kmeans
import numpy
import sys
## step 1: load data  
print "step 1: load data..."  
dataSet = []  
fileIn = open('tmp.txt')  
for line in fileIn.readlines():  
    lineArr = line.strip().split(',')  
    dataSet.append([float(lineArr[0]), float(lineArr[1])])  
  
## step 2: clustering...  
print "step 2: clustering..."  
dataSet = mat(dataSet)  
k = 3  
centroids, clusterAssment = kmeans.kmeans(dataSet, k)
clusterAssment_=numpy.array(clusterAssment)

## step 3: show the result  
print "step 3: show the result..."  
kmeans.showCluster(dataSet, k, centroids, clusterAssment)  


with open('tmp_.txt', 'w+') as file:
    sys.stdout = file  #标准输出重定向至文件
    for i in range(835):
        print(clusterAssment_[i][0],round(clusterAssment_[i][1],2))
    print(centroids)
