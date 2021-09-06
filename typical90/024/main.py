N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dif = [abs(a - b) for a, b in zip(A, B)]
if sum(dif) <= K:
    if (K - sum(dif)) % 2 == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')