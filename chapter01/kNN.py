from numpy import *
import operator
import logging



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
        #print("i :",i)
        voteIlabel = labels[sortedDistIndicies[i]]
        #print("------ voteIlabel:",voteIlabel)
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        classCountTwo = classCount.items()
        #print("------ classCountTwo:",classCountTwo)
        sortedClassCount = sorted(classCountTwo, key=operator.itemgetter(1), reverse=True)
        #print("------ sortedClassCount:",sortedClassCount)
    return sortedClassCount[0][0]
#根据计算出的距离，将标签排序。迭代取得前三个标签，将标签放入一个字典，key为标签，value为标签出现的次数，次数在迭代中累加。
#items函数返回可遍历的元组数组，然后将其按第二个纬度进行排序，也就是字典中的value，即按标签出现次数降序排列。然后取得出现次数最多的标签返回。


def  file2matrix(filename):                              #读取数据，将其分别放如不同变量中
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
         line = line.strip()                                #取出一行数据删除空白格
         #print("line : ",line)
         listFromLine = line.split('\t')                    #将line按制表符分割
         #print("listFromLine : ",listFromLine)
         returnMat[index,:] = listFromLine[0:3]             #将前三个字段取出放入零矩阵的相应位置
         #print("returnMat : ",returnMat)
         classLabelVector.append(int(listFromLine[-1]))     #将最后一个字段取出放入列表中
         #print("classLabelVector : ",classLabelVector)
         index += 1
    return returnMat,classLabelVector


def autoNorm(dataSet):                                    #将数据进行归一化处理，使其分类精度提高
    minVals = dataSet.min(0)
    #print("minVals : ",minVals)
    maxVals = dataSet.max(0)
    #print("maxVals : ",maxVals)
    ranges = maxVals - minVals
    #print("ranges : ",ranges)
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    #print("m ：",m)
    normDataSet = dataSet - tile(minVals,(m,1))             #将第一个纬度复制m次，将 第二个纬度复制1次
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals

def datingClassTest():
     hoRatio = 0.10
     datingDataMat,datingLabels = file2matrix('F:\python\machinelearninginaction\Ch02\datingTestSet2.txt')            #读取数据并初步处理
     normMat, ranges, minVals = autoNorm(datingDataMat)                                                               #归一化
     m = normMat.shape[0]
     numTestVesc = int(m*hoRatio)
     errorCount = 0
     for i in range(numTestVesc):                                                                                    #迭代进行分类并检测
          classifierResult = classify0( normMat[i,:], normMat[numTestVesc:m,:], datingLabels[numTestVesc:m],3)
          print("the classifier came back with: %d, the real answer is: %d" % (classifierResult,datingLabels[i]))
          if(classifierResult !=  datingLabels[i]):errorCount += 1.0
          print("the total error rate is : %f " % (errorCount/float(numTestVesc)))


def classifyPerson():
     resultList  = ['not at all', 'in small doses', 'in large doses']
     percentTats = float(input("percentage of time spent playing video games ?"))
     ffMiles     = float(input("frequent flier miles earned per year ?"))
     iceCream    = float(input("liters of ice cream consumed per year ?"))
     datingDataMat, datingLabels = file2matrix('F:\python\machinelearninginaction\Ch02\datingTestSet2.txt')
     normMat, ranges, minVals = autoNorm(datingDataMat)
     inArr = array([ffMiles,percentTats,iceCream])
     classifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels, 3)
     print("You will probably like this person: ",resultList[classifierResult-1])


def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in  range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
        return returnVect

#手写数字识别，测试代码
def  handwritingClassTest():
      hwLabels = []
      trainingFileList = os.listdir('F:\python\machinelearninginaction\Ch02\\trainingDigits')
      m = len(trainingFileList)
      trainingFileList = zeros((m,1024))











