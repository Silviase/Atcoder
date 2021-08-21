"""
添字と文字の二つ組をPriorityQueueに入れて、
何文字目までみたかをみてやればいい
"""
import heapq


def get_tuple(s):
    res = []
    for i in range(len(s)):
        res.append((s[i], i))
    return res


N, K = map(int, input().split())
S = input()
t = get_tuple(S)
hq = []
heapq.heapify(hq)
idx = -1
res = []
for i in range(N - K):
    heapq.heappush(hq, t[i])
for i in range(N - K, N):
    heapq.heappush(hq, t[i])
    while True:
        c, j = heapq.heappop(hq)
        if idx < j:
            idx = j
            res.append(c)
            break
print(''.join(res))