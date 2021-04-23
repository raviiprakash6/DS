def pairWithGivenSum(arr,sum):
    set1=set()
    for i in arr:
        if i not in set1:
            set1.add(i)

    for i in arr:
        set1.remove(i)
        if sum-i in set1:
            return "Yes"
    return "NO"

arr=[10,5,6]
print(pairWithGivenSum(arr,11))