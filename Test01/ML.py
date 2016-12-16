from numpy import *
randMat = mat(random.rand(4,4))
print(randMat)
invRandMat = randMat.I
print(randMat* invRandMat)
myEye = randMat * invRandMat
print(myEye - eye(4))


