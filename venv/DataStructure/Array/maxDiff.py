def maxDiff(arr):
    maxval = arr[1] - arr[0]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[j] - arr[i] > maxval):
                maxval = arr[j] - arr[i]
    return maxval




#----------------------------------------------------------------------------------------------------------------

def maxDiff(arr):
    maxdiff=arr[1]-arr[0]
    minval=arr[0]
    for i in range(1,len(arr)):
        if(arr[i-1]<minval):
            minval=arr[i-1]
        if(arr[i]-minval>maxdiff):
            maxdiff=arr[i]-minval


    return maxdiff