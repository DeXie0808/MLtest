from numpy import *
import operator
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group , labels

def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]                                      #求出全部样数
    diffMat = tile(inX,(dataSetSize,1)) - dataSet                       #将待分类样本重复，然后与已知样本相减
    sqDiffMat = diffMat**2                                              #得出的向量每一个数求平方
    sqDistances = sqDiffMat.sum(axis=1)                                 #将新向量的每一个数相加
    distances = sqDistances**0.5                                        #得出的数开平方
    sortedDistIndicies = distances.argsort()                            #返回数组从小到大的索引值
    classCount={}                                                       #样本距离计算完成
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        classCountTwo = classCount.items()
        sortedClassCount = sorted(classCountTwo, key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]




def  file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
         line = line.strip()
         listFromLine = line.split('\t')
         returnMat[index,:] = listFromLine[0:3]
         classLabelVector.append(int(listFromLine[-1]))
         index += 1
    return returnMat,classLabelVector



def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals