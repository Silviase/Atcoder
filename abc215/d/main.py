import math


def bunkai(N):
    res = []
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            res.append(i)
            while N % i == 0:
                N //= i
    if N > 1:
        res.append(N)
    return set(res)


def hurui(M, used_prime):
    cand = list(range(1, M))
    for p in used_prime:
        cand = list(filter(lambda x: x % p != 0, cand))
    return cand


N, M = map(int, input().split())
A = list(map(int, input().split()))

used_prime = []

for a in A:
    used_prime += bunkai(a)

used_prime = set(used_prime)
# 使った素数は全てused_primeに含まれている
# print(prime_set)
res = hurui(M, used_prime)
print(len(res))
for r in res:
    print(r)