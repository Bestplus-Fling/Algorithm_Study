import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
#########################################
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def BFS(x, y, p):
    queue = deque([[x, y]])
    checker[x][y] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < N):
                continue
            if checker[nx][ny] or data[nx][ny] <= p:
                continue
            queue.append([nx, ny])
            checker[nx][ny] = True


N = int(input())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_height = 0
for i in range(N):
    for j in range(N):
        if data[i][j] > max_height:
            max_height = data[i][j]
result = 0
for k in range(0, max_height+1):
    checker = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if checker[i][j]: continue
            if data[i][j] <= k: continue
            BFS(i, j, k)
            cnt += 1
    result = max(cnt, result)
print(result)