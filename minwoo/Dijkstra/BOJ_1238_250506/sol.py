import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(vertex, c):
    global graph, INF, X, N
    distances = [INF] * (N + 1)
    queue = [(0, vertex)]
    distances[vertex] = 0
    while queue:
        dist, vtx = heapq.heappop(queue)
        if dist > distances[vtx]:
            continue
        for adj, w in graph[vtx]:
            if (acc := dist + w) >= distances[adj]:
                continue
            heapq.heappush(queue, (acc, adj))
            distances[adj] = acc
    if c == 'return':
        return distances[::]
    return distances[c]


N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for s, e, t in [tuple(map(int, input().split())) for _ in range(M)]:
    graph[s].append((e, t))
result = 0

back = dijkstra(X, 'return')
for v in range(1, N+1):
    if v == X:
        continue
    cnt = dijkstra(v, X) + back[v]
    result = max(cnt, result)
print(result)
