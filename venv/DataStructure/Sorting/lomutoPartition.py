def lomutoPartition(arr,low,high):
    """This function takes last element as pivot, places
    the pivot element at its correct position in sorted"""
    i=0
    temp=0
    pivot=arr[high]
    for j in range(high):
        if(arr[j]<pivot):
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
            i+=1
    arr[high]=arr[i]
    arr[i]=pivot
    return i

arr=[1,6,2,8,4]
print(lomutoPartition(arr,0,4))



            

