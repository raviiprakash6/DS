def moveAllZeros(arr):
    n=len(arr)
    i=0
    j=0
    while(i<n):
        if arr[i]!=0 and arr[j]!=0:
            i+=1
            j+=1
        elif arr[j]==0 and arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j=j+1
            i=i+1
        elif arr[i]==0 and arr[j]==0:
            i+=1
    return arr

#arr=[10,20]
arr=[1,2,0,0,6,8,0,1]
print(moveAllZeros(arr))



####################-----------------O(n)----------------------------------------########################
def moveAllZeros(arr):
    n=len(arr)
    j=0
    for i in range(0,n):
        if (arr[i]!=0):
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr
