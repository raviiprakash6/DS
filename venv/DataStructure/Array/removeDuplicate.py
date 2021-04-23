def removeDuplicate(arr):
    b=[]
    b.append(arr[0])
    for i in arr:
        if(i not in b):
            b.append(i)
    return b


#*****************------------------------------------********************************

removeDuplicate = list(dict.fromkeys(arr))
