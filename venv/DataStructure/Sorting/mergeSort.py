def lomuto(arr,max,min):
    pivot=arr[max]

    i,j=0,0
    while(i<max):
        if(arr[i]<pivot):
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j+=1
        else:
            i+=1
    arr[max],arr[j]=arr[j],pivot
    return j

def mergesort(arr,max,min):
    if(max>min):
        i=lomuto(arr,max,min)
        mergesort(arr,max,i+1)
        mergesort(arr,i-1,min)
    return  arr



##################################################################################
def mergeSort(arr):
    n=len(arr)

    if(n>1):
        mid=n//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        arr1=left
        arr2=right
        n1 = len(arr1)
        n2 = len(arr2)
        i = 0
        j = 0
        k = 0
        while (i < n1 and j < n2):
            if (arr1[i] <= arr2[j]):
                arr[k]=arr1[i]
                i += 1
                k += 1
            else:
                arr[k]=arr2[j]
                j += 1
                k += 1
        while (i < n1):
            arr[k]=arr1[i]
            i = i + 1
            k += 1
        while (j < n2):
            arr[k]=arr2[j]
            j += 1
            k += 1
        return arr


arr=[90,1,2,5,67,98]
print(mergeSort(arr))