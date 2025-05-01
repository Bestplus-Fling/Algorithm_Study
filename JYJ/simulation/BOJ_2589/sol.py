import sys
sys.stdin = open('input.txt', 'r')
#########################################
from collections import deque
dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def bfs(i, j, depth):
    global max_len
    queue.append([i, j, depth])
    visited[i][j] = 1
    while queue:
        x, y, depth = queue.popleft()
        max_len = max(max_len, depth)
        depth += 1
        for dx, dy in dxy:
            ni = x + dx
            nj = y + dy

            if not(0 <= ni < n and 0 <= nj < m): continue

            if visited[ni][nj] == 1: continue

            if arr[ni][nj] == 'W': continue

            visited[ni][nj] = 1
            queue.append([ni, nj, depth])


n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
queue = deque()
max_len = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            visited = [[0] * m for _ in range(n)]
            bfs(i, j, 0)
print(max_len)
