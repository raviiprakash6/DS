def quickSort(arr,low,high):
    """This is implementation of quicksort using Lomutopartition"""
    if(low<high):

        i=low
        pivot=arr[high]
        for j in range(low,high):
            if(arr[j]<pivot):
                arr[j],arr[i]=arr[i],arr[j]
                i+=1
        arr[high],arr[i]=arr[i],arr[high]
        partition=i
        #partition=lomutoPartition.lomutoPartition(arr,low,high)
        quickSort(arr,low,partition-1)
        quickSort(arr,partition+1,high)
        return arr

arr=[1,2,3,4,5,6,-1,-3]
print(quickSort(arr,0,7))