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



#--------------------------
def fib(n):
    a=0
    b=1
    c=0
    for i in range(n):
        if i==0:
            c=a
        elif i==1:
            c=b
        else:
            c=a+b
            a=b
            b=c
    return c


#---------------------------
def fib(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    return fib(n-1, b, a + b)

