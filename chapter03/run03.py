from imp import reload
import chapter03.trees
str='-------------------'

reload(chapter03.trees)
myDat,labels = chapter03.trees.createDataSet()
print(chapter03.trees.calcShannonEnt(myDat))

myDat,labels = chapter03.trees.createDataSet()
print(myDat)
chapter03.trees.splitDataSet(myDat,0,1)
print(str)
print(chapter03.trees.chooseBestFeatureToSplit(myDat))