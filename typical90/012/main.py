class Union_find_tree:
    def __init__(self, H, W):
        self.par = [i for i in range(H * W)]
        self.rank = [0 for _ in range(H * W)]
        self.h = H
        self.w = W
        self.colored = [False for _ in range(H * W)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def colorize(self, x):
        self.colored[x] = True
        neighbors = [x - 1, x + 1, x - self.w, x + self.w]
        for nei in neighbors:
            if 0 <= nei < self.h * self.w and self.colored[nei]:
                self.unite(x, nei)


class Grid:
    def __init__(self, H, W):
        self.H = H
        self.W = W

    def to_index(self, h, w):
        return h * self.W + w


H, W = list(map(int, input().split()))
Q = int(input())
UFT = Union_find_tree(H, W)
G = Grid(H, W)
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        query_type, x, y = q[0], q[1] - 1, q[2] - 1
        p = G.to_index(x, y)
        UFT.colorize(p)
    else:
        query_type, x1, y1, x2, y2 = q[
            0], q[1] - 1, q[2] - 1, q[3] - 1, q[4] - 1
        p1 = G.to_index(x1, y1)
        p2 = G.to_index(x2, y2)
        if UFT.colored[p1] and UFT.colored[p2] and UFT.same(p1, p2):
            print('Yes')
        else:
            print('No')
