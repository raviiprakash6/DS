def unionOfTwoUnsortedArray(arr1,arr2):
    set1=set()
    for i in arr1:
        if i not in set1:
            set1.add(i)
    for i in arr2:
        if i in set1:
            set1.remove(i)
            print(i)



arr1=[1,4,1,3]
arr2=[1,2,3,2,1]
unionOfTwoUnsortedArray(arr1,arr2)
