N = int(input())
res, num = 0, 1
while num <= N:
    res += 1
    num *= 2
print(res - 1)
