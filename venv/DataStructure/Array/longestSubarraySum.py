def longestSubarraySum(arr, sum1):
    dict1 = {}
    max_len = 0
    length = 0
    elemSum = 0
    for i in range(len(arr)):
        elemSum = elemSum + arr[i]
        if elemSum == sum1:
            length = i + 1
        elif elemSum - sum1 in dict1.keys():
            length = i - dict1[elemSum - sum1]
        elif elemSum not in dict1:
            dict1[elemSum]=i
        max_len = max(length, max_len)
    return max_len


arr = [8,3,7]
sum1= 15
print(longestSubarraySum(arr, sum1))
