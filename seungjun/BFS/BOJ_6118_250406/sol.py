import sys
sys.stdin = open('input.txt', 'r')
######################################
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# 1 base
visited = [0] * (n + 1)
queue = deque()

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 시작점 1, cnt 0
visited[1] = -1
queue.append((1, 0))

# BFS 탐색
while queue:
    now, cnt = queue.popleft()

    cnt += 1
    for adj_v in graph[now]:
        if visited[adj_v]: continue
        visited[adj_v] = cnt
        queue.append((adj_v, cnt))

# 숨어야 하는 헛간 번호, 헛간 과의 거리, 목표 헛간과 거리가 같은 헛간의 개수
result_1 = 0
result_2 = -float('inf')
result_3 = 0
for i in range(n + 1):
    if result_2 > visited[i]: continue
    if result_2 < visited[i]:
        result_1 = i
        result_2 = visited[i]
        result_3 = 1
    elif result_2 == visited[i]:
        result_3 += 1

print(result_1, result_2, result_3)