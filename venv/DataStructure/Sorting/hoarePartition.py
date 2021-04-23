def hoarePartition(arr,low,high):
    """This function takes first element as pivot and
    places smaller element to
     """
    i=1
    j=high
    pivot=arr[0]
    while(i<j):
        while(arr[i]<pivot):
            i+=1
        while(arr[j]>pivot):
            j-=1
        if(i>=j):
            return arr,i,j
        else:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i+=1
            j-=1
    arr[low]=arr[j]
    arr[j]=pivot

    return arr,j

arr=[5,12,1,2,3,4,8,20,21]
print(hoarePartition(arr,0,8))

