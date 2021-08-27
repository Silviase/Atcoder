import heapq


class Graph:
    def __init__(self, size):
        self.size = size
        self.dist = [[0 for i in range(size)] for j in range(size)]
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
