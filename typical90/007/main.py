def complaint(A, B):
    # A is the sorted array of the number
    # B is the number to be searched
    # return difference from the nearest number
    ng = -1
    ok = len(A)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if B < A[mid]:
            ok = mid
        else:
            ng = mid
    res = 1e9
    if ng >= 0:
        res = min(res, abs(B - A[ng]))
    if ok < len(A):
        res = min(res, abs(B - A[ok]))
    return res


N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
for _ in range(Q):
    B = int(input())
    print(complaint(A, B))