from imp import reload
import matplotlib
import matplotlib.pyplot as plt
import chapter01.kNNtest
from numpy import array
import os

group,labels = chapter01.kNNtest.createDataSet()

print(chapter01.kNNtest.classify0([0.1,0.1],group,labels,3))

reload(chapter01.kNNtest)
datingDataMat,datingLabels = chapter01.kNNtest.file2matrix('F:\python\machinelearninginaction\Ch02\datingTestSet2.txt')
print(datingDataMat,datingLabels)
