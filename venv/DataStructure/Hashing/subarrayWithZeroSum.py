def subarrayWithZeroSum(arr):
    temp=set()
    presum=0
    for i in arr:
        presum=presum+i
        if presum in temp or presum==0:
            return "sub array with sum zero is present"
        temp.add(presum)
    return "No sub array with zero sum"

arr=[1,2,-3,4,5]
print(subarrayWithZeroSum(arr))


