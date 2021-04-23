def majorityElement(arr):
    """A majority element in an array A[] of size n is an element that
       appears more than n/2 times (and hence there is at most one such element)"""

    i=arr[0]
    n=len(arr)
    count=1
    for j in range(1,len(arr)):
        if(arr[j]==arr[j-1]):
            count=count+1
            elem=arr[j]
        else:
            count=count-1
    if(count>0):
        print(elem)
    else:
        print(False)


arr=[2,2,2,2,3,3,3]
majorityElement(arr)



#####################Naive Approach####################
# def majorityElement(arr):
#
#     Elem=-1
#     n=len(arr)
#     for i in range(n):
#         count=0
#         for j in range(i,n):
#           if(arr[i]==arr[j]):
#               count+=1
#         if(count > n/2):
#             Elem=arr[i]
#     return  print(Elem)
#
# arr=[2,2,2,2,3,3,3]
# majorityElement(arr)

