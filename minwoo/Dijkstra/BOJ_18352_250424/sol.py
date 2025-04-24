import sys
import heapq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dijkstra():
    global N, graph, X, K
    distances = {z: float('inf') for z in range(1, N+1)}
    queue = [(0, X)]
    distances[X] = 0
    while queue:
        dist, vtx = heapq.heappop(queue)
        if dist > distances[vtx]:
            continue
        for adj, w in graph[vtx]:
            acc = dist + w
            if acc >= distances[adj]:
                continue
            heapq.heappush(queue, (acc, adj))
            distances[adj] = acc
    result = []
    for i in range(1, N+1):
        if distances[i] == float('inf'):
            continue
        if distances[i] == K:
            result.append(i)
    if result:
        return result
    return [-1]


N, M, K, X = map(int, input().split())
graph = {v: [] for v in range(1, N+1)}
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append((y, 1))
print(*dijkstra(), sep='\n')
