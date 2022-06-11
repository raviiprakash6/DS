def reverseInteger(x):
    '''Reverse integer and check range in [-2^31, 2^31 - 1] '''
    val = int(str(x)[::-1]) if x > 0 else int(str(x * -1)[::-1]) * -1
    return val if -(2 ** 31) - 1 < val < 2 ** 31 else 0




###################################


def reverseInteger(x):
    s = (x > 0) - (x < 0)
    r = int(str(x*s)[::-1])
    return s*r * (r < 2**31)