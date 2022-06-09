def intToRoman(num: int):
    '''Given an integer, convert it to a roman numeral.'''
    arr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ''
    i = 0
    while (num > 0):
        if arr[i] <= num:
            res += roman[i]
            num = num - arr[i]
        else:
            i += 1
    return res


print(intToRoman(1994))