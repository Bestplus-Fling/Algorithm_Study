import sys
sys.stdin = open('input.txt', 'r')
######################################
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
# 그래프 선언, 1 base
graph = [[] for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)
# print(graph)

# bfs 탐색
queue = deque()
max_hacking = 0
candidates = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)

    visited[i] = True
    hacking = 1
    queue.append(i)

    while queue:
        vertex = queue.popleft()

        for adj_v in graph[vertex]:
            if visited[adj_v]: continue
            hacking += 1
            visited[adj_v] = True
            queue.append(adj_v)

    if max_hacking < hacking:
        max_hacking = hacking
        candidates = [i]
    elif max_hacking == hacking:
        candidates.append(i)

print(*candidates)