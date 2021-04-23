def infiniteSizeArray(arr,elem):
    i=1
    prev=0
    if(arr[0]==elem):
        return 0
    while(arr[i]):
        if(arr[i]==elem):
            return i
        elif(arr[i]<elem):
            prev=i
            i=i*2
        else:
            low=prev
            high = i - 1
            while (low <= high):
                mid = int((low + (high)) / 2)
                if (arr[mid] == elem):
                    return mid
                elif (elem > arr[mid]):
                    low = mid + 1
                elif (elem < arr[mid]):
                    high = mid - 1
            return -1
