# remove duplicates from sorted array

def removeDuplicateSorted(arr):
    res=[]
    n=len(arr)
    res.append(arr[0])
    for i in range(n):
        if(arr[i]!=res[i-1]):
            res.append(arr[i])
    return res

#---------------------------------------------------------------------------------

def removeDuplicateSorted(arr):
    res=[]
    res.append(arr[0])
    n=len(arr)
    for i in range (1,n):
        if(arr[i]-arr[i-1]!=0):
            res.append(arr[i])
    return res


