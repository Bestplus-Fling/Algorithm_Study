import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def bfs(vtx):
    global graph, V
    visited = [0] * V
    queue = deque([vtx])
    while queue:
        vtx = queue.popleft()
        for adj in range(V):
            if graph[vtx][adj] > 0:
                if visited[adj]: continue
                queue.append(adj)
                visited[adj] = 1
    return visited


V = int(input())
graph = [list(map(int, input().split())) for _ in range(V)]
for i in range(V):
    print(' '.join(map(str, bfs(i))))
