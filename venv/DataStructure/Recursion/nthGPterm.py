import math


def nthGPterm(n, firstTerm, commonRatio):

    return ( firstTerm * (int)(math.pow(commonRatio, n - 1)))

print(nthGPterm(4,2,2))


