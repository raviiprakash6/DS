from collections import deque


def maximumOfSubarray(arr, k):
    n = len(arr)
    de = deque()
    for i in range(k):
        # (While de) will check if any sequence is empty
        while de and arr[i] >= arr[de[-1]]:
            de.pop()
        de.append(i)

    for j in range(k, n):
        print(arr[de[0]])
        while de and de[0] <= j - k:
            de.popleft()
        while de and arr[j] >= arr[de[-1]]:
            de.pop()
        de.append(j)
    print(arr[de[0]])


arr = [12, 6, 2, 8, 17,6,7,1,4]
maximumOfSubarray(arr, 3)
