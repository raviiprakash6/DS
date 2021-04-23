def subsets(nums):
    n = len(nums)
    subset = [[]]
    for i in nums:
        list=[]
        for j in subset:
            list += [[i] + j]
        subset = subset + list
    return subset


arr=[1,2]
print(subsets(arr))


