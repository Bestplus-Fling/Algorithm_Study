import sys
sys.stdin = open('input.txt', 'r')
import heapq
input = sys.stdin.readline


def dijkstra():
    global graph, distances, stv
    queue = [(0, stv)]
    heapq.heapify(queue)
    distances[stv] = 0
    while queue:
        dist, vtx = heapq.heappop(queue)
        if dist > distances[vtx]:
            continue
        for adj, w in graph[vtx]:
            acc = w + dist
            if acc >= distances[adj]: continue
            heapq.heappush(queue, (acc, adj))
            distances[adj] = acc


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distances = {v: float('inf') for v in range(1, N+1)}
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
stv, edv = map(int, input().split())
dijkstra()
print(distances[edv])
