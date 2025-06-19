import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
INF = float('inf')

# a 집하장에서 b 집하장까지 최단거리로 이동하기 위해서
# 가장 먼저 방문하는 정점이 궁금하다.
# 해당 정점으로 가기 위해 이동한 경로도 알아야 한다.


def dijkstra(s):
    global graph, chart
    distance = {v: INF for v in range(1, N+1)}
    q = [(0, s)]
    distance[s] = 0
    prev = [0] * (N+1)
    while q:
        dist, vtx = heapq.heappop(q)
        if dist > distance[vtx]:
            continue
        for adj, w in graph[vtx]:
            if (acc := dist + w) >= distance[adj]:
                continue
            prev[adj] = vtx
            heapq.heappush(q, (acc, adj))
            distance[adj] = acc
            if vtx == s:
                prev[adj] = adj
            else:
                prev[adj] = prev[vtx]
    print(prev)
    return prev


N, M = map(int, input().split())
graph = {v: set() for v in range(1, N+1)}
chart = []
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].add((v, w))
    graph[v].add((u, w))
for i in range(1, N+1):
    row = []
    res = dijkstra(i)
    for j in range(1, N+1):
        if i == j:
            row.append('-')
            continue
        row.append(str(res[j]))
    chart.append(' '.join(row))
print('\n'.join(chart))
