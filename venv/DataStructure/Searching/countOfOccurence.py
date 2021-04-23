def countOfOccurence(arr, elem, high, low=0):
    """Given a sorted array and an element we need to count occurrences of element in the array"""
    count = 0
    i = 0
    while (low <= high):
        mid = int((high + low) / 2)
        if ((mid == 0 and arr[mid] == elem) or
                (arr[mid] == elem and arr[mid] != arr[mid - 1])):
            while (high >= mid + i and arr[mid] == arr[mid + i]):
                count = count + 1
                i = i + 1
            return count

        elif (elem > arr[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return -1


#---------------------------------------------------------------------------------------------------
