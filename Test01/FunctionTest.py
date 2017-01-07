# -*- coding: utf-8 -*-
from numpy import *
import operator
#shape
'''
A = [[1],[2]]
print(shape(A))

#zeros
A=zeros(5)
print(A,int8)

t1=tuple("helloworld")
print(t1)

a = [[1,1],[2,2],[3,3],[4,4]]
b = operator.itemgetter(2,3)
print(b(a))

a={}
a[1]=5
a[2]=10
b = a.items()
print(b)


#python 冒泡排序
array = [1, 2, 5, 3, 6, 8, 4]
for i in range(len(array) - 1, 0, -1):
    print("i :" , i)
    for j in range(0, i):
        print("j :" , j)
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)


a=zeros((5,3))
print(a)

for a in range(1,10):
    print(a)

a = float(input("shu ru :"))
print(a)


b = zeros((2,10))
print(b)


str='wang qin he'
print(str.split(' ',1),)

a=[1,2,3]
b=[4,5,6]
a.extend(b)

print(a)

for i in range(5):
    print(i)


dataSet = [[1,1,'yes'],[1,0,'no'],[1,1,'no'],[0,1,'yes'],[0,1,'no'],[1,0,'no']]
print(len(dataSet[0]))


'''
abc = {'wang','qin','qin',6}
print(abc)

bcd = set([5,5,6,7,8,9,9,'wang','qin'])
print(bcd-abc)
bef = set('a')
bef.add('a')
print(bef)














