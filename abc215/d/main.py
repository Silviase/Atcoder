def hurui(A, M):
    res = list(range(1, M + 1))
    print(" ".join(res))
    for a in A:
        res = list(filter(lambda x: x % a != 0, res))
        print(" ".join(res))
    return res


N, M = map(int, input().split())
A = list(set(map(int, input().split())))
A = list(filter(lambda x: x != 1, A))

res = hurui(A, M)
print(" ".join(res))