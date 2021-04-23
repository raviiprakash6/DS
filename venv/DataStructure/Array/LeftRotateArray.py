#Complexity-O(n)
#Aux space-O(1)


def leftRotateByD(arr,d):
    n=len(arr)
    def reverse(arr,first,last):
        while(first<=last):
            arr[first],arr[last]=arr[last],arr[first]
            first+=1
            last-=1

    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)

    return arr


arr=[1,2,3,4]
print(leftRotateByD(arr,2))




#---------------------------------------------------------------------
#Complexity-O(n)
#Aux space-O(n)

def leftRotatebyOne(arr):
    """Given an array of size n left rotate the array by 1"""
    res=[]
    n=len(arr)
    for i in range(n-1):
        res.append(arr[i+1])
    res.append(arr[0])
    return res




