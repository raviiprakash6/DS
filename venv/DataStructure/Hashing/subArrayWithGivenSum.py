def subArrayWithGivenSum(arr,sum):
    presum=0
    dic=dict()
    n=len(arr)
    for i in range(n):
        presum=presum+arr[i]
        dic[presum]=i
        v=presum-sum
        #Presum == sum is to handle corner case
        #If presum-sum is present in presum list then we have subarray present
        if v in dic.keys() or presum == sum:
            return "subarray with given sum present"

    return "No subarray with given sum present"

arr=[3,1,1,8]
print(subArrayWithGivenSum(arr,6))
