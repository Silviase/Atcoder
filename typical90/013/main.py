import heapq


class Graph:
    def __init__(self, size):
        self.size = size
        self.adj = [[] for _ in range(size)]

    def add_edge(self, src, dest, weight):
        self.adj[src].append((dest, weight))

    def add_undirected_edge(self, src, dest, weight):
        self.add_edge(src, dest, weight)
        self.add_edge(dest, src, weight)

    def dijkstra(self, src):
        dist = [float('inf') for _ in range(self.size)]
        dist[src] = 0
        visited = [False for _ in range(self.size)]
        pq = [(0, src)]
        while pq:
            w, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            for v, wt in self.adj[u]:
                if dist[v] > dist[u] + wt:
                    dist[v] = dist[u] + wt
                    heapq.heappush(pq, (dist[v], v))
        return dist


N, M = map(int, input().split())
G = Graph(N)
for _ in range(M):
    a, b, c = map(int, input().split())
    G.add_undirected_edge(a - 1, b - 1, c)
dist_from_1 = G.dijkstra(0)
dist_from_N = G.dijkstra(N - 1)
for i in range(N):
    print(dist_from_1[i] + dist_from_N[i])