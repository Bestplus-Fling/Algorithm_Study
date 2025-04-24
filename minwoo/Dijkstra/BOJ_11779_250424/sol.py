import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def dijkstra():
    global graph, distance, stv, edv
    queue = [(0, stv, [stv])]
    distance[stv] = 0
    temp = []
    while queue:
        dist, vtx, channel = heapq.heappop(queue)
        if dist > distance[vtx]: continue
        for adj, w in graph[vtx]:
            if (acc := dist + w) >= distance[adj]:
                continue
            heapq.heappush(queue, (acc, adj, channel+[adj]))
            distance[adj] = acc
            if adj == edv:
                temp = channel + [adj]
    return temp


N = int(input())
graph = {v: [] for v in range(1, N+1)}
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
stv, edv = map(int, input().split())
distance = {v: float('inf') for v in range(1, N+1)}
short_channel = dijkstra()
print(distance[edv])
print(len(short_channel))
print(*short_channel)
