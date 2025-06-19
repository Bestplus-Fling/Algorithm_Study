import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
INF = float('inf')


def dist(x):
    global graph
    q = deque([(x, 0)])
    arr[x][x] = 0
    while q:
        vtx, c = q.popleft()
        c += 1
        for adj in graph[vtx]:
            if arr[adj][x] != INF:
                continue
            q.append((adj, c))
            arr[adj][x] = c


N, M, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
arr = [[-1] * (N+1) for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
arr = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    dist(i)
for _ in range(Q):
    u, v = map(int, input().split())
    ans = INF
    for i in range(1, N+1):
        ut, vt = arr[u][i], arr[v][i]
        if INF in [ut, vt]:
            continue
        ans = min(ans, max(ut, vt))
    print(ans if ans != INF else -1)
