def longestSubArrayWithGivenSum(arr,sum):
    dic=dict()
    n=len(arr)
    presum=0
    maxlength=0
    for i in range(n):
        presum=presum+arr[i]
        if sum==presum:
            length=i+1
            maxlength=max((maxlength,length))
        if presum-sum in dic.keys():
            length=i-dic[presum-sum]
            maxlength=max(maxlength,length)
        if presum not in dic.keys():
            dic[presum]=i

    return maxlength


arr=[3,1,0,1,8,2,3,6]
print(longestSubArrayWithGivenSum(arr,5))
    