from numpy import  *
import operator
import os

def createDataSet():
    group  =array([[1.0,1.1],[1.0,1.0],[0.0,0.0],[0.0,0.1]])
    labels=['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):                  #(待分类样本,全部样本，全部标签 ，近邻个数)
    dataSetSize = dataSet.shape[0]
    dataMat = tile(inX,(dataSetSize,1)) - dataSet       #将inX重复全部样本个数次，每次重复纬度为1.并与测试样本相减
    sqDiffMat = dataMat**2                              #结果求平方
    sqDistances = sqDiffMat.sum(axis=1)                 #axis=1是将矩阵每一行相加的意思。
    distances = sqDistances**0.5                        #将结果开平方
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1  #将标签放入字典，然后反复迭代该标签出现次数
        classCountTwo = classCount.items()
        sortedClassCount = sorted(classCountTwo,key=operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    arrayOLine = fr.readlines()
    numberOfLines = len(arrayOLine)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLine:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    minValue = dataSet.min(0)
    maxValue = dataSet.max(0)
    ranges = maxValue - minValue
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minValue,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minValue

def datingClassTest():
    hoRoit = 0.10
    dataMat,dataLabels = file2matrix('F:\python\machinelearninginaction\Ch02\datingTestSet2.txt')
    normDataSet ,ranges, minValue = autoNorm(dataMat)
    dataMatSize = dataMat.shape[0]
    testDataSize = int(dataMatSize*hoRoit)
    errorCount = 0
    for i in range(testDataSize):
        classifyResult = classify0(normDataSet[i,:],normDataSet[testDataSize,:dataMatSize:],dataLabels[testDataSize:dataMatSize],3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifyResult, dataLabels[i]))
        if (classifyResult != dataLabels[i]): errorCount += 1.0
        print("the total error rate is : %f " % (errorCount/float(testDataSize)))




