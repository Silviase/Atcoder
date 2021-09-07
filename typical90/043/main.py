import heapq
"""
方針としては曲がる回数の少ない順にPriorityQueueに入れてやればよさそう，
入れる必要があるのは(i, j, move_type, dist)である
"""

DEBUG = True


def make_next_move(dist, r, c, move_type):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    next_move = []
    for i in range(4):
        next_move.append((dist + 1 if move_type != i else dist,
                          (r + dx[i], c + dy[i], move_type)))

    return next_move


H, W = map(int, input().split())
rs, cs = map(lambda x: int(x) - 1, input().split())
rt, ct = map(lambda x: int(x) - 1, input().split())

grid = [list(input()) for _ in range(H)]
visited = [[1e9] * W for _ in range(H)]
pq = [(0, (rs, cs, i)) for i in range(4)]
heapq.heapify(pq)

print(pq)

while pq:
    dist, (r, c, move_type) = heapq.heappop(pq)
    if r < 0 or r >= H or c < 0 or c >= W:
        continue
    if grid[r][c] == '#':
        continue
    if dist > visited[r][c]:
        continue
    else:
        visited[r][c] = dist
    if DEBUG:
        print("NEW POINT", dist, r, c, move_type)
    next_move = make_next_move(dist, r, c, move_type)
    if DEBUG:
        print("ADD")
        for i in next_move:
            print("\t", i)
    for nm in next_move:
        heapq.heappush(pq, nm)
    if DEBUG:
        print("AFTER ADD", pq)

print(visited[rt][ct])