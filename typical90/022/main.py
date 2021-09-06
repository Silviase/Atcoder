def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


A, B, C = map(int, input().split())
r = gcd(gcd(A, B), C)
print(A // r + B // r + C // r - 3)
