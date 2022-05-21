def sumOfKconsecutiveElem(arr,k):
    '''Sliding widow technique'''
    n=len(arr)
    sum=0
    maxSum=0
    for i in range(0,k):
        sum+=arr[i]
    maxSum=max(maxSum,sum)
    for i in range(k,n):
        sum=sum-arr[i-k]+arr[i]
        maxSum=max(maxSum,sum)

    return maxSum


arr=[5,-10,6,90,3]
print(sumOfKconsecutiveElem(arr,2))