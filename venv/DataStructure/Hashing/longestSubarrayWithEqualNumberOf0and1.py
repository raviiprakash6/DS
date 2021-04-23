def longestSubarrayWithEqualNumberOf0and1(arr):
    dic=dict()
    n=len(arr)
    presum=0
    maxlength=0
    length=0
    for i in range(n):
        if arr[i]==1:
            presum=arr[i]+presum
        else:
            presum=presum-1
        if presum==0:
            length=i+1
            maxlength = max(length, maxlength)
        if presum not in dic.keys():
            dic[presum]=i
        else:
            length=i-dic[presum]
            maxlength=max(length,maxlength)
    return maxlength

arr=[0,0,1,1,1,1,1,0]
print(longestSubarrayWithEqualNumberOf0and1(arr))

