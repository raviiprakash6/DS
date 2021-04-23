def countInversionInArray(arr):
    """A pair i,j form an inversion when i<j and arr[i]>arr[j] """
    n=len(arr)
    count=0
    for i in range(n):
        for j in range(i,n):
            if(j>i and arr[i]>arr[j]):
                count+=1
    return count


arr=[40,30,20,10]
print(countInversionInArray(arr))