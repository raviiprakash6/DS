def intersectionOfTwoSortedArray(arr1,arr2):
    """This function will give you intersection of two sorted array
    If the number is repetetive  it should appear only once in output"""
    n1=len(arr1)
    n2=len(arr2)
    i=0
    j=0
    temp=[]
    while(i<n1 and j<n2):
        #If you check the duplicate of one array you don't have to check for other
        if(i>0 and arr1[i]==arr1[i-1]):
            i+=1
        elif(j>0 and arr2[j]==arr2[j-1]):
            j+=1
        elif(arr1[i]==arr2[j]):
            temp.append(arr1[i])
            i+=1
            j+=1
        elif(arr1[i]>arr2[j]):
            j+=1
        else:
            i+=1
    return temp


arr1=[1,2,2,3,5]
arr2=[2,2,4,6,7]

print(intersectionOfTwoSortedArray(arr1,arr2))



