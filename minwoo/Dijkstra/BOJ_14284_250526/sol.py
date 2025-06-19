import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
INF = float('inf')


def dijkstra(stv, edv):
    global graph, N
    distance = {v: INF for v in range(1, N+1)}
    distance[stv] = 0
    q = [(0, stv)]
    while q:
        d, vtx = heapq.heappop(q)
        if d > distance[vtx]:
            continue
        for adj, w in graph[vtx]:
            if (acc := w + d) >= distance[adj]:
                continue
            heapq.heappush(q, (acc, adj))
            distance[adj] = acc
    return distance[edv]


N, M = map(int, input().split())
graph = {v: [] for v in range(1, N+1)}
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
print(dijkstra(*map(int, input().split())))
