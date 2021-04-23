def countOfDistinctElement(arr):
    set1=set()
    n=len(arr)
    count=0
    for i in range(n):
        if(arr[i] not in set1):
            set1.add(arr[i])
            count+=1
    return count

if __name__ =='__main__':
    arr=[1,2,2,4,6,7,4,1]
    print(countOfDistinctElement(arr))
