# coding:utf8
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from sklearn import metrics

dataSet=[]
fileIn = open('tmp.txt')  
for line in fileIn.readlines():  
    lineArr = line.strip().split(',')  
    dataSet.append([float(lineArr[0]), float(lineArr[1])])  
#print dataSet
dataSet = np.mat(dataSet)
K = range(1, 20)
meandistortions = []
for k in K:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(dataSet)
    # 求kmeans的成本函数值
    meandistortions.append(sum(np.min(cdist(dataSet, kmeans.cluster_centers_, 'euclidean'), axis=1)) / dataSet.shape[0])
#print(meandistortions)
# 说不清它应该聚类成2、3、4个点，因此我们需要通过分别计算k=(2,3,4)的聚类结果，并比较他们的成本函数值，随着k的增大，成本函数值会不断降低，只有快速降低的那个k值才是最合适的k值

plt.figure()
plt.grid(True)
plt1 = plt.subplot(2,1,1)
# 画样本点
plt1.plot(dataSet[:,0],dataSet[:,1],'k.');
plt2 = plt.subplot(2,1,2)
# 画成本函数值曲线
plt2.plot(K, meandistortions, 'bx-')
plt.show()


plt.figure(figsize=(8, 10)) 
plt.subplot(3, 2, 1)
x1=dataSet[:,0]
x2=dataSet[:,1]
X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)


'''
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']
markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']
tests = [2, 3, 4, 5, 8]
subplot_counter = 1
for t in tests:
    subplot_counter += 1
    plt.subplot(3, 2, subplot_counter)
    kmeans_model = KMeans(n_clusters=t).fit(X)
    for i, l in enumerate(kmeans_model.labels_):
        plt.plot(x1[i], x2[i], color=colors[l], marker=markers[l],ls='None')
        #print(t,metrics.silhouette_score(X, kmeans_model.labels_,metric='euclidean'))
        plt.title('k= %s,轮廓系数　= %0.3f' %(t,metrics.silhouette_score(X,kmeans_model.labels_,metric='euclidean'),fontproperties=font))
'''
