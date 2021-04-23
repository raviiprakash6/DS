def squareRoot(elem):
    low=0
    high=elem
    while(low<=high):
        mid=int((low+high)/2)
        if((mid*mid)==elem or((mid*mid)<elem<((mid+1)*(mid+1)))):
            return mid
        elif((mid*mid)>elem):
            high=mid-1
        else:
            low=mid+1



#---------------------------------------------------------------------------------------------

def squareRoot(elem):
    for i in range(elem):
        if((i*i)>elem):
            return i-1

print(squareRoot(5))