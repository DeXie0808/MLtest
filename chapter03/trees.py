from math import log

#香农熵的计算
def calcShannonEnt(dataSet):                          #计算给定数据集的香农熵
    numEntries = len(dataSet)                           #计算出数据集长度
    labelCounts = {}                                    #新建字典
    for featVec in dataSet:                            #遍历数据集
        currentLabel = featVec[-1]                      #查询数据的最后一列
        if currentLabel not in labelCounts.keys():     #如果数据存在字典则key +1 ,如何不存在，则将数据放入字典且key设为0
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0                                    #计算香农熵
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

#测试香农熵计算
def createDataSet():
    dataSet = [[1,1,'yes'],[1,0,'no'],[1,1,'yes'],[0,1,'no'],[0,1,'no']]
    labels = ['no  surfacing','flippers']
    return dataSet,labels


def splitDataSet(dataSet , axis , value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    print(retDataSet)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):                      #选择最好的数据集划分方式
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0;  bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i]  for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature