from typing import Deque
from numpy import argmax


def bfs(start, adjs):
    dist = [-1 for i in range(len(adjs))]
    dist[start] = 0
    queue = Deque([start])
    while queue:
        u = queue.popleft()
        for v in adjs[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    return argmax(dist), max(dist)


# 木において、任意に選んだ頂点をAとすると、Aから最も遠い頂点Bから最も遠い頂点Cについて、BCの長さが木の直径である。
# 木の直径を2回のBFSで求める。開始点は0とする。
def longest_circular_load(N, adjs):
    idx, dist = bfs(0, adjs)
    idx, dist = bfs(idx, adjs)
    return dist + 1


N = int(input())
adjacent = [[] for _ in range(N)]
for i in range(N - 1):
    A, B = map(lambda x: int(x) - 1, input().split())
    adjacent[A].append(B)
    adjacent[B].append(A)

print(longest_circular_load(N, adjacent))