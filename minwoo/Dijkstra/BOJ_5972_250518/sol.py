import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
INF = float('inf')


def f():
    q = [(0, 1)]
    heapq.heapify(q)
    distance[1] = 0
    while q:
        dist, vertex = heapq.heappop(q)
        if dist > distance[vertex]:
            continue
        for adj, d in graph[vertex]:
            if (acc := d + dist) >= distance[adj]:
                continue
            heapq.heappush(q, (acc, adj))
            distance[adj] = acc


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N + 1)
for m in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
f()
print(distance[N])


