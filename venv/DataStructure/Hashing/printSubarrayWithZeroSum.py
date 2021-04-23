def printSubarrayWithZeroSum(arr):
    dic = dict()
    sum = 0
    for i in arr:
        sum = sum + i
        if sum in dic.keys() or sum == 0:
            return arr[dic.get(sum)+1:i+1]
        dic[sum]=i
    return "No sub array with zero sum"

#Incomplete---------
arr = [1, 2, -3, 4, 5]
print(subarrayWithZeroSum(arr))

