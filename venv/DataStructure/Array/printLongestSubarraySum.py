def printLongestSubarraySum(arr, sum1):
    dict1 = {}
    max_len = 0
    length = 0
    elemSum = 0
    initial_index=0
    final_index=0
    for i in range(len(arr)):
        elemSum = elemSum + arr[i]
        if elemSum == sum1:
            length = i + 1
            if length > max_len:
                initial_index=0
                final_index=i+1
                max_len=length

        elif elemSum - sum1 in dict1.keys():
            length = i - dict1[elemSum - sum1]
            if length > max_len:
                initial_index=dict1[elemSum - sum1]+1
                final_index=i+1
                max_len=length
        elif elemSum not in dict1:
            dict1[elemSum]=i


    return arr[initial_index:final_index]


arr = [8,3,7,3,2]
sum1= 13
print(printLongestSubarraySum(arr, sum1))
