def sumOfDigit(num,sum=0):
    if num ==0:
        return sum

    return sumOfDigit(num//10,sum+num%10)

print(sumOfDigit(000000))