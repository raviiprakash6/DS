def maxLengthEvenOddArray(arr):
    count=1
    res=1
    for i in range(1,len(arr)):
        if (arr[i]%2==0 and arr[i-1]%2!=0) or (arr[i]%2!=0 and arr[i-1]%2==0) :
            count+=1
        else:
            count=1
        res=max(res,count)
    return res

arr=[22,32,44,56]
print(maxLengthEvenOddArray(arr))
