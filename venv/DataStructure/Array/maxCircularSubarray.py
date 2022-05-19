def maxCircularSubarray(arr):
    n = len(arr)
    maxsum = 0

    for i in range(n):
        sum = 0
        for j in range(n):
            index = (i + j) % n
            sum = sum + arr[index]
            if (sum > maxsum):
                maxsum = sum

    return maxsum

arr=[5,-2,3,4]
print(maxCircularSubarray(arr))



##########################################################
def maxCircularSubarrayEfficientSoln(arr):
    presum=0
    minsum=0
    sum=0
    for i in range(0,len(arr)):
        sum+=arr[i]
        presum=min(arr[i],arr[i]+presum)
        minsum=min(minsum,presum)

    return sum-minsum


print(maxCircularSubarrayEfficientSoln(arr))


