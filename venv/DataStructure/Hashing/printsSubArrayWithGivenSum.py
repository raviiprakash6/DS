def printSubArrayWithGivenSum(arr,sum):
    presum=0
    dic=dict()
    n=len(arr)
    for i in range(n):
        presum=presum+arr[i]
        dic[presum]=i
        v=presum-sum
        if v in dic.keys():
            return arr[dic.get(v):i+1]

    return "No subarray with given sum present"

arr=[1,2,2,-2,3]
print(subArrayWithGivenSum(arr,5))
