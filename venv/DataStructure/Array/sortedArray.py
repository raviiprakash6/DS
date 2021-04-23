def sortedArray(arr):
    """This function check if the given array is sorted or not"""
    flag = True
    n=len(arr)
    for i in range(1,n):
        if (arr[i-1] > arr[i]):
            flag = False
            break;

    return flag


print(sortedArray([1,2,4,3]))