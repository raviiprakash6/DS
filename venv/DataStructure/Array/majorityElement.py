def majorityElement(arr):
    """A majority element in an array A[] of size n is an element that
       appears more than n/2 times (and hence there is at most one such element)"""
    Elem=-1
    count = 1
    count1 = 0
    elemIndex = 0
    n = len(arr)
    for j in range(1, n):
        if arr[j] == arr[j - 1]:
            count = count + 1
        else:
            count = count - 1

        if count == 0:
            elemIndex = j
            count = 1

    if count > 0:
        for i in range(0, n):
            if arr[i] == arr[j]:
                count1 += 1
        if count1 > n / 2:
            Elem = arr[i]
    return print(Elem)



arr = [6,8,7,6,6]
majorityElement(arr)


#####################Naive Approach####################
def majorityElementNaiveSoln(arr):
    Elem = -1
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(i, n):
            if (arr[i] == arr[j]):
                count += 1
        if (count > n / 2):
            Elem = arr[i]
    return print(Elem)


majorityElementNaiveSoln(arr)
