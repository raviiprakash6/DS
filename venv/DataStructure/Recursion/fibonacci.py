#####------iterative way to print fibonacci------
def fibonacci(n):
    arr = []
    if n <=0:
        return "Enter number greater than 0"
    elif(n==1 or n==2):
        for i in range(n):
            arr.append(i)
        return arr
    else:
        arr.append(0)
        arr.append(1)
        for i in range(2, n):
            arr.append(arr[i - 1] + arr[i - 2])

    return arr


#print(fibonacci(5))
#***************************using recursion to get number**************************
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-2)+fibonacci(n-1)

print(fibonacci(4))

