import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def prim(edges):
    global V
    mst = 0
    adj_list = {v: [] for v in range(1, V+1)}
    for stv, edv, w in edges:
        adj_list[stv].append((edv, w))
        adj_list[edv].append((stv, w))

    visited = set()
    pq = [(w, 1, e) for e, w in adj_list[1]]
    heapq.heapify(pq)
    visited.add(1)

    while pq:
        weight, stv, edv = heapq.heappop(pq)
        if edv in visited: continue

        visited.add(edv)
        mst += weight

        for adj_v, adj_w in adj_list[edv]:
            if adj_v in visited: continue
            heapq.heappush(pq, (adj_w, edv, adj_v))
    return mst


V, E = map(int, input().split())
print(prim([tuple(map(int, input().split())) for _ in range(E)]))

