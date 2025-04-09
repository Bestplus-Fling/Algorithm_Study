import sys
sys.stdin = open('input.txt','r')
#########################################
import sys
input = sys.stdin.readline
from collections import deque

# 입력
r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

# BFS 탐색 준비
escape = 'IMPOSSIBLE'
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[False] * c for _ in range(r)]
queue = deque()
# 지훈 or 불 위치, type_, time
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'J':
            visited[i][j] = True
            queue.append((i, j, 'J', 1))
        if arr[i][j] == 'F':
            visited[i][j] = True
            queue.appendleft((i, j, 'F', 1))

while queue:
    i, j, type_, time = queue.popleft()

    # type_ 'J' 및 위치가 가장자리면 탈출 가능
    if type_ == 'J':
        if i == 0 or j == 0 or i == r - 1 or j == c - 1:
            escape = time
            break

    # 델타 탐색
    for dy, dx in dxy:
        ni, nj = i + dy, j + dx
        if ni < 0 or nj < 0 or r <= ni or c <= nj:
            continue
        if arr[ni][nj] == '#':
            continue
        if visited[ni][nj]:
            continue
        visited[ni][nj] = True
        queue.append((ni, nj, type_, time + 1))

print(escape)