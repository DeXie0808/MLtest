from imp import reload
import chapter03.trees
import chapter03.treePlotter
str='-------------------'




reload(chapter03.trees)
myDat,labels = chapter03.trees.createDataSet()
print(chapter03.trees.calcShannonEnt(myDat))

myDat,labels = chapter03.trees.createDataSet()
print(myDat)
print(chapter03.trees.splitDataSet(myDat,0,1))

print(chapter03.trees.chooseBestFeatureToSplit(myDat))
print(str)


#----------Decision tree
myDat,labels = chapter03.trees.createDataSet()
myTree = chapter03.trees.createTree(myDat,labels)
print(myTree)

#----------绘制决策树
chapter03.treePlotter.createPlot()