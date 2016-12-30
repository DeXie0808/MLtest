from imp import reload
import chapter03.trees

reload(chapter03.trees)
myDat,labels = chapter03.trees.createDataSet()
print(chapter03.trees.calcShannonEnt(myDat))

reload(chapter03.trees)
myDat,labels = chapter03.trees.createDataSet()
print(myDat)
chapter03.trees.splitDataSet(myDat,0,0)