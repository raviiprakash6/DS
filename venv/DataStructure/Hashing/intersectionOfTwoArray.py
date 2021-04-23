def intersectionOfTwoArray(arr1,arr2):
    set1=set()
    count=0

    for i in arr1:
        if i not in set1:
            set1.add(i)
    for i in arr2:
        if i in set1:
            set1.remove(i)
            count+=1

    return print(count)


arr1=[1,4,1,3]
arr2=[1,2,3,2,1]
intersectionOfTwoArray(arr1,arr2)


# def intersectionOfTwoArray(array1,array2):
#     set1=set()
#     for i in array1:
#         if i in array2:
#             set1.add(i)
#     return len(set1)
#
