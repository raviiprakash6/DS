def mergeTwoSortedArray(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0
    temp = []
    while(i < n1 and j < n2):
        if (arr1[i] <= arr2[j]):
            temp.append(arr1[i])
            i += 1
        else:
            temp.append(arr2[j])
            j += 1
    while(i < n1):
        temp.append(arr1[i])
        i=i+1
    while(j < n2):
        temp.append(arr2[j])
        j+=1
    return temp

arr1=[10,13,14]
arr2=[11,15,17]
print(mergeTwoSortedArray(arr1, arr2))
