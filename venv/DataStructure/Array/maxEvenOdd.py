def maxEvenOdd(arr, c=1):
    """This function will return you longest length of contiguous even and odd number"""
    n = len(arr)
    count = 1
    res = 1
    for i in range(c, n):
        if ((arr[i - 1] - arr[i]) % 2 != 0):
            count = count + 1

        else:
            count = 1
        res = max(res, count)

    return res


#-----------------------------------------------------------Recursion-------------------------------

def maxEvenOdd(arr, c=1):
    """This function will return you longest length of  contiguous even and odd number"""
    n = len(arr)
    count = 1
    if (c <= n - 1):
        for i in range(c, n):
            if ((arr[i - 1] - arr[i]) % 2 != 0):
                count = count + 1
                c = i + 1
            else:
                c = i + 1
                break
    else:
        # When number of element in list1 is 1 function will diectly come out from this return
        return 1
    return max(count, maxEvenOdd(arr, c))


#-------------------------------------------------------------------------------------------------------#

def maxEvenOdd(arr,c=1):
    """This function will return you longest length of  contiguous even and odd number"""
    n=len(arr)
    b=1
    if(c<=n-1):
        for i in range(c,n):
            if((arr[i-1]%2==0 and arr[i]%2!=0) or
               (arr[i-1]%2!=0 and arr[i]%2==0)):
                b=b+1
                c=i+1
            else:
                c=i+1
                break;
    else:
        #When number of element in list1 is 1 function will diectly come out from this return
        return 1
    return max(b,maxEvenOdd(arr,c))

arr=[1]
print(maxEvenOdd(arr))

