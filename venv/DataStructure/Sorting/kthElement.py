def kthElement(arr,low,high,k):
    if(low<high):

        i=low
        temp=0
        pivot=arr[high]

        for j in range(low,high):
            if(arr[j]<pivot):
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
                i+=1

        arr[high]=arr[i]
        arr[i]=pivot
        par=i


        if(par==k):
            return arr,arr[par]
        elif(k<par):
            kthElement(arr,low,par-1,k)
        else:
            kthElement(arr,par+1,high,k)

    return arr,arr[k]


arr=[3,7,1,2,16]
print(kthElement(arr,0,4,4))

