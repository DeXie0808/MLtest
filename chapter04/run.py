import chapter04.bayes
from numpy import *

listOPosts, listClasses = chapter04.bayes.loadDataSet()
myVocabList = chapter04.bayes.createVocabList(listOPosts)
print(myVocabList)

listA = chapter04.bayes.setOfWords2Vec(myVocabList,listOPosts[0])
print(listA)
listB = chapter04.bayes.setOfWords2Vec(myVocabList,listOPosts[5])
print(listB)

listOPosts,listClasses = chapter04.bayes.loadDataSet()
