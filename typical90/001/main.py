def yokan_party_check(N, K, A, mid):
    # 長さがmid以上でカウントを足す。K回カウントできればTrue
    count = 0
    check = 0
    for i in range(len(A)):
        if A[i] - check >= mid:
            count += 1
            check = A[i]
            #print("cut", A[i])
    #print(count, mid)
    return count > K


def yokan_party(N, L, K, A):
    # 長さXでK＋１個の分割ができるかどうかを確かめる
    # 二分探索で求める,  分割できるならより大きいXを探す
    min = 1
    max = L
    while abs(max - min) > 1:
        mid = (max + min) // 2
        if yokan_party_check(N, K, A, mid):
            min = mid
        else:
            max = mid
    return min


N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
A.append(L)
#print(A)
res = yokan_party(N, L, K, A)
print(res)
