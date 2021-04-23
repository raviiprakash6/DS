def maxSubArraySum(arr):
    lastsum = 0
    maxsum =arr[0]
    for i in arr:
        lastsum = max(i, i + lastsum)
        if (lastsum > maxsum):
            maxsum = lastsum
    return maxsum

arr=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArraySum(arr))

#-----------------------------------------------------------------------------------------------
# def maxSubArraySum(arr):
#     n = len(arr)
#     maxsum = arr[0]
#
#     for i in range(n):
#         lastsum=0
#         for j in range(i,n):
#             lastsum = arr[j] + lastsum
#         if (lastsum > maxsum):
#             maxsum = lastsum
#     return maxsum

