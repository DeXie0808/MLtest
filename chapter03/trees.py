from math import log
import operator

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
    #dataSet = [[1,1,'yes'],[1,0,'no'],[1,1,'no'],[0,1,'yes'],[0,1,'no'],[1,0,'no'],[2,3,'no'],[4,7,'yes']]
    #dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    dataSet = [[1,1,'maybe'],[2,2,'maybe'],[1,0,'no'],[0,1,'yes'],[0,2,'yes'],[3,2,'no'],[1,4,'yes']]
    labels = ['no  surfacing','flippers']
    return dataSet,labels


def splitDataSet(dataSet , axis , value):            #划分数据集并(数据集，待分类的特征，期望分类的值)
    retDataSet = []                                    #划分的数据集序列
    for featVec in dataSet:
        if featVec[axis] == value:                     #如果当前数据集元素特征值等于value
            reducedFeatVec = featVec[:axis]            #
            reducedFeatVec.extend(featVec[axis+1:])    #将特征值取出,其他特征放在一个新的列表里
            retDataSet.append(reducedFeatVec)          #将该列表放入返回数据集中
    return retDataSet


def chooseBestFeatureToSplit(dataSet):                          #选择最好的数据集划分方式
    numFeatures = len(dataSet[0]) - 1                               #计算数据集的特征个数
    baseEntropy = calcShannonEnt(dataSet)                           #计算数据集原始香农熵
    bestInfoGain = 0.0;  bestFeature = -1                           #
    for i in range(numFeatures):                                   #遍历数据集特征
        featList = [example[i]  for example in dataSet]            #遍历数据集所有元素的当前特征的值
        uniqueVals = set(featList)                                  #将值放入集合中
        newEntropy = 0.0                                            #
        for value in uniqueVals:                                   #遍历特征值
            subDataSet = splitDataSet(dataSet,i,value)              #用当前特征和特征值将数据集进划分
            prob = len(subDataSet)/float(len(dataSet))              #计算当前划分出的数据集元素出现的概率
            newEntropy += prob * calcShannonEnt(subDataSet)         #概率 * 香农熵 相加
        infoGain = baseEntropy - newEntropy                         #和原始熵值相比较
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i                                         #遍历时计算最佳特征
    return bestFeature                                             #返回最佳特征




def majorityCnt(classList):                                       #返回输入列表的key出现次数,降序排列
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reversed = True)
    return sortedClassCount[0][0]



#--------------------Decision tree
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in  dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree

