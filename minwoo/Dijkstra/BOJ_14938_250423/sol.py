import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def dijkstra(stv):
    global graph, R, MAP, M
    distances = {v: float('inf') for v in range(1, N + 1)}
    queue = [(0, stv)]
    heapq.heapify(queue)
    distances[stv] = 0
    cnt = 0
    while queue:
        dist, vtx = heapq.heappop(queue)
        if dist > distances[vtx]: continue
        for adj, w in graph[vtx]:
            acc = dist + w
            if distances[adj] <= acc: continue
            heapq.heappush(queue, (acc, adj))
            distances[adj] = acc
    for i in range(1, N+1):
        if distances[i] <= M:
            cnt += MAP[i-1]
    return cnt


N, M, R = map(int, input().split())
MAP = list(map(int, input().split()))
graph = {v: [] for v in range(1, N+1)}
for _ in range(R):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))
result = 0
for i in range(1, N+1):
    result = max(result, dijkstra(i))
print(result)

