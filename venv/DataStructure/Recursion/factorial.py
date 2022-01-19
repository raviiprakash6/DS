# Tail recursion
def factorial(n, a=1):
    if n == 0:
        return a
    elif n == 1:
        return a
    return factorial(n - 1, a * n)


print(factorial(100))


# Recursion

def factorial(n):
    if n == 0:
        return 1

    return factorial(n - 1) * n


print(factorial(995))
