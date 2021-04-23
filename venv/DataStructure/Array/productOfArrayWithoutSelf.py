def productOfArrayWithoutSelf(arr):
    """This programme return an array output such that output[i] is
     equal to the product of all the elements of nums except arr[i]"""
    n=len(arr) #4
    leftProduct=[0]*n
    rightProduct=[0]*n
    output=[0]*n
    leftProduct[0]=1
    rightProduct[n-1]=1
    # for i in range(1,n):
    #     leftProduct[i]=leftProduct[i-1]*arr[i-1]
    for i in range(n-2,-1,-1):
        rightProduct[i]=rightProduct[i+1]*arr[i+1]
    for i in range(n):
        output[i]=leftProduct[i]*rightProduct[i]
    return output

arr=[1,2,3,4]
print(productOfArrayWithoutSelf(arr))



