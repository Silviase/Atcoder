def range_sum(acc, l, r):
    return acc[r] - acc[l - 1]


def make_acc(A):
    res = [0 for _ in range(len(A) + 1)]
    for i in range(len(A)):
        res[i + 1] = res[i] + A[i]
    return res


N = int(input())
c1 = [0 for _ in range(N)]
c2 = [0 for _ in range(N)]
for i in range(N):
    cl, p = map(int, input().split())
    if cl == 1:
        c1[i] = p
    else:
        c2[i] = p
c1_acc, c2_acc = make_acc(c1), make_acc(c2)
Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    c1 = range_sum(c1_acc, l, r)
    c2 = range_sum(c2_acc, l, r)
    print(c1, c2)