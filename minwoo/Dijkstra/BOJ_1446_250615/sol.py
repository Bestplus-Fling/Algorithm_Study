import sys
import heapq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float('inf')
MAX = 10009


def dijkstra():
    global edges, D
    distance = [INF] * MAX
    hq = [(0, 0)]
    distance[0] = 0
    while hq:
        d, cur = heapq.heappop(hq)
        if d > distance[cur]: continue
        for nxt, w in edges[cur]:
            if nxt > D or cur >= nxt or (acc := d + w) >= distance[nxt]:
                continue
            heapq.heappush(hq, (acc, nxt))
            distance[nxt] = acc
        # 지름길 없이 1 이동하는 경우
        if cur + 1 <= D and d + 1 < distance[cur + 1]:
            heapq.heappush(hq, (d+1, cur+1))
            distance[cur+1] = d + 1
    return distance[D]


N, D = map(int, input().split())
edges = [[] for _ in range(MAX)]
for n in range(N):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))
print(dijkstra())