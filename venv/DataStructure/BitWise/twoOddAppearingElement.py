arr = [5, 2, 2, 3, 3, 4, 4, 6]
xor = 0
for i in arr:
    xor = xor ^ i
print(xor)
i = xor
p = 0
while (pow(2, p) != i & pow(2, p)):
    p += 1
z = pow(2, p)
print(z)
res1 = 0
res2 = 0
for i in arr:
    if (z & i) == 0:
        res1 = res1 ^ i
    else:
        res2 = res2 ^ i
print(res1, res2)


