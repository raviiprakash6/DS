# def maxDiff(arr):
#     maxval = arr[1] - arr[0]
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if (arr[j] - arr[i] > maxval):
#                 maxval = arr[j] - arr[i]
#     return maxval
#
#
#

#----------------------------------------------------------------------------------------------------------------

def maxDiff(arr):
    maxdiff=arr[1]-arr[0]
    minval=arr[0]
    for i in range(1,len(arr)):
        if(arr[i-1]<minval):
            minval=arr[i-1]
        if(arr[i]-minval>maxdiff):
            maxdiff=arr[i]-minval


    return maxdiff




arr = [2,3,10,6,4,8,1]
print(maxDiff(arr))


#------------------------------------------------------------------------------------
#Find the largest element from right and smallest element from left and return max-min

def maxDiff(arr):
    i = 0
    j = len(arr) - 1
    max_val = arr[j]
    min_val = arr[0]
    while i < j:
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[j] > max_val:
            max_val = arr[j]

        j = j - 1
        i = i + 1
    print(i)
    print(j)
    return max_val - min_val

