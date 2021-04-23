def chocolateDistribution(arr,low,high,m):
    i=low
    pivot=arr[high]
    if(low<high):
        for j in range(low,high):
            if(arr[j]<pivot):
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
                i+=1
        arr[high]=arr[i]
        arr[i]=pivot
        partition=i
        chocolateDistribution(arr, 0, partition-1,m)
        chocolateDistribution(arr, partition+1, high,m)
        minval = arr[m-1] - arr[0]
        for i in range(high+1-m):
            if((arr[m-1+i]-arr[i])<minval):
                minval = arr[m-1+i] - arr[i]

        return arr,minval

arr=[1,8,2,18,12,3]
print(chocolateDistribution(arr,0,5,4))