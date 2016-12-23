from imp import reload
import matplotlib
import matplotlib.pyplot as plt
import chapter01.kNN
from numpy import array
import os

group,labels= chapter01.kNN.createDataSet()

#K-近邻法
print(chapter01.kNN.classify0([0,0],group,labels,3))

#改进约会网站匹配效果
reload(chapter01.kNN)
datingDataMat,datingLabels = chapter01.kNN.file2matrix('F:\python\machinelearninginaction\Ch02\datingTestSet2.txt')
#print(datingDataMat,datingLabels)


#matplotlib 创建散点图
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels), 15.0*array(datingLabels)) #画散点图，
plt.xlabel("games")
plt.ylabel("ice cream")
#plt.show()


#归一化数值
reload(chapter01.kNN)
normMat , ranges , minVals = chapter01.kNN.autoNorm(datingDataMat)
#print(normMat,ranges,minVals)


#测试算法
#chapter01.kNN.datingClassTest()

#输入数据，生成结果
#chapter01.kNN.classifyPerson()

#手写数字识别
chapter01.kNN.handwritingClassTest()
