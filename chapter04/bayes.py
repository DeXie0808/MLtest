def loadDataSet():         #获取样本
    postingList = [['my','dog','has','flea',\
                    'problems','help','please'],
                    ['maybe','not','take','him',\
                   'to','dog','park','stupid'],
                    ['my', 'dalmation', 'is', 'so', 'cute',\
                     'I','love','him'],
                    ['stop','posting','stupid','worthless','garbage'],
                    ['mr','licks','ate','my','steak','how',\
                     'to','stop','him'],
                    ['quit', 'buying', 'worthless','dog','food','stupid']]

    classVec = [0,1,0,1,0,1]  #0代表侮辱性语言，1代表正常语言
    return postingList,classVec

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWords2Vec(vocabList,inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print ("the word %s is not in my vocabList " % word)
    return returnVec




