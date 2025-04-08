import sys
sys.stdin = open('input.txt', 'r')
######################################
import sys
input = sys.stdin.readline
from collections import deque

# 입력, 인접 행렬
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 방향성 그래프
graph = [[] for _ in range(n)]
for vertex, adj_arr in enumerate(arr):
    for idx, adj_v in enumerate(adj_arr):
        if adj_v:
            graph[vertex].append(idx)

# BFS 탐색
queue = deque()
for i in range(n):
    visited = [False] * n
    queue.append(i)

    while queue:
        vertex = queue.popleft()

        for adj in graph[vertex]:
            if visited[adj]: continue
            arr[i][adj] = 1
            visited[adj] = True
            queue.append(adj)
# 인접 행렬
for i in arr:
    print(*i)
