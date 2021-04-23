def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        temp=arr[i]
        while(i>0 and arr[i-1]>temp):
            arr[i]=arr[i-1]
            arr[i-1]=temp
            i-=1
    return arr

arr=[1,5,3,7,9,2]
print(insertionSort(arr))
