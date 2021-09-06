class Graph:
    def __init__(self, size):
        self.size = size
        # self.dist = [[0 for i in range(size)] for j in range(size)]
        self.adj = [[] for _ in range(size)]

    def add_edge(self, src, dest, weight):
        self.adj[src].append((dest, weight))

    def add_undirected_edge(self, src, dest, weight):
        self.add_edge(src, dest, weight)
        self.add_edge(dest, src, weight)

    def bfs(self, src):
        visited = [False for _ in range(self.size)]
        dist = [float('inf') for _ in range(self.size)]
        dist[src] = 0
        queue = [src]
        visited[src] = True
        while queue:
            u = queue.pop(0)
            for v, wt in self.adj[u]:
                if visited[v]:
                    continue
                visited[v] = True
                dist[v] = dist[u] + wt
                queue.append(v)
        return dist


N = int(input())
G = Graph(N)
for _ in range(N - 1):
    l, r = map(lambda x: int(x) - 1, input().split())
    G.add_undirected_edge(l, r, 1)

d0 = G.bfs(0)
odd_from_0 = [i for i in range(N) if d0[i] % 2 == 1]
evn_from_0 = [i for i in range(N) if d0[i] % 2 == 0]

if len(odd_from_0) >= (N // 2):
    for v in odd_from_0[:N // 2]:
        print(v + 1, end=" ")
else:
    for v in evn_from_0[:N // 2]:
        print(v + 1, end=" ")
