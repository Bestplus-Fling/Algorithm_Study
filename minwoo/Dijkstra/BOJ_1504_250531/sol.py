import sys
import heapq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

"""
방향성 없는 그래프
1번에서 N번으로
임의로 주어진 두 정점은 반드시 통과해야 한다
"""
INF = float('inf')


def dijkstra(s, e):
    global graph
    distance = {v: INF for v in range(1, N+1)}
    q = [(0, s)]
    heapq.heapify(q)
    distance[s] = 0
    while q:
        d, vtx = heapq.heappop(q)
        if d > distance[vtx]:
            continue
        for adj, w in graph[vtx]:
            if (acc := d + w) >= distance[adj]:
                continue
            heapq.heappush(q, (acc, adj))
            distance[adj] = acc
    return distance[e]


N, E = map(int, input().split())
graph = {v: set() for v in range(1, N+1)}
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].add((b, c))
    graph[b].add((a, c))
v1, v2 = map(int, input().split())
r1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
r2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)
ans = min(r1, r2)
print(ans if ans != INF else -1)
