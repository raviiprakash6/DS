

def leaderInArray(arr):
    """
An element is called the leader of an array if there is no element greater than it on the right side."""
    a=len(arr)
    b=[]
    c=arr[a-1]
    b.append(c)
    for i in range(a-2,-1,-1):
        if(arr[i]>c):
            b.append(arr[i])
            c=arr[i]
    return b


# -------------------------------------------------------------------------------------------------------
def leaderInArray(arr):
    a = len(arr)
    b = []

    for i in range(a):
        flag = True
        for j in range(i + 1, a):
            if (arr[i] < arr[j]):
                flag = False
                print(arr[i])
                break;
        if (flag == True or i == a - 1):
            b.append(arr[i])

    return b


