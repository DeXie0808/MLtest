def triangles(x):
    L1=[0,1]
    n=0
    while n<x:
        print(L1[1:])
        n=n+1
        L2=L1.append(0)
        L1=[L1[i-1]+L1[i] for i in range(len(L1))]

    n = 0
    for t in triangles():
        print(t)
        n = n + 1
        if n == 10:
            break
