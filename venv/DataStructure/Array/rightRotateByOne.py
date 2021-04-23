def rightRotatebyOne(arr):
    b=[]
    b.append(arr[-1])
    for i in range(len(arr)-1):
        b.append(arr[i])
    return b
