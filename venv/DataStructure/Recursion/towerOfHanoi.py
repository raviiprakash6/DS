def towerOfHanoi(n,a,b,c):
    if n>0:
        towerOfHanoi(n-1,a,c,b)
        print(n,"move a disc from {} to {}".format(a,c))
        towerOfHanoi(n-1,b,a,c)



print(towerOfHanoi(4,'A','B','C'))