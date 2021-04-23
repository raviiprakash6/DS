def naturalNumberSum(num,k=0):
    if num==0:
        return k

    return naturalNumberSum(num-1,k+num)

print(naturalNumberSum(8))