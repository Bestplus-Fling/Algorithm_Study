import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    global graph, N, check
    q = []
    heapq.heappush(q, (0, 0))
    distances = {v: INF for v in range(N)}
    distances[0] = 0
    while q:
        d, vtx = heapq.heappop(q)
        if d > distances[vtx]:
            continue
        for adj, w in graph[vtx]:
            if adj != N-1 and check[adj] == 1:
                continue
            if (acc := d + w) >= distances[adj]:
                continue
            heapq.heappush(q, (acc, adj))
            distances[adj] = acc
    if (x := distances[N - 1]) != INF:
        return x
    return -1


N, M = map(int, input().split())
check = list(map(int, input().split()))

graph = {v: set() for v in range(N)}
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].add((b, t))
    graph[b].add((a, t))

print(dijkstra())