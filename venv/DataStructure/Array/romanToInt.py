def romanToInt(s):
    res, prev = 0, 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in s[::-1]:  # rev the s
        if dict[i] >= prev:
            res += dict[i]  # sum the value iff previous value same or more
        else:
            res -= dict[i]  # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc
        prev = dict[i]
    return res


s = "III"
print(romanToInt(s))


#################################
def romanToInt(s):
    arr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    i = 0
    j = 0
    sum = 0
    n = len(s)
    while j <= n - 1:
        if roman[i] == s[j]:
            sum += arr[i]
            j += 1
        elif roman[i] == s[j:j + 2]:
            sum += arr[i]
            j += 2
        else:
            i += 1
    return sum
