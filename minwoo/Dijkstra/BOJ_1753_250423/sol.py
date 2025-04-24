import sys
sys.stdin = open('input.txt', 'r')
import heapq
input = sys.stdin.readline


def dijkstra():
    global stv, graph, distances
    queue = [(0, stv)]
    heapq.heapify(queue)
    distances[stv] = 0
    while queue:
        weight, vtx = heapq.heappop(queue)
        if distances[vtx] < weight:
            continue
        for adj, w in graph[vtx]:
            acc = weight + w
            if acc >= distances[adj]:
                continue
            heapq.heappush(queue, (acc, adj))
            distances[adj] = acc


N, M = map(int, input().split())
stv = int(input())
graph = [[] for _ in range(N+1)]
distances = {v: float('inf') for v in range(1, N+1)}
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
dijkstra()
for i in range(1, N+1):
    if distances[i] == float('inf'):
        print('INF')
    else:
        print(distances[i])
