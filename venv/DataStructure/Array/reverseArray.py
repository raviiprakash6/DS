#using for loop
def reverseArray(lis):
    res=[]
    n=len(lis)
    for i in range(n-1,-1,-1):
        res.append(lis[i])
    return res
###################Reverse Array using index#########################
def reverseArray(arr):

    return arr[::-1]

#print(reverse([1,2,3]))

