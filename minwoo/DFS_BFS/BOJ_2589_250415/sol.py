import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(ix, iy):
    global grid, R, C, max_value
    visited = [[False] * C for _ in range(R)]
    queue = deque([(ix, iy, 0)])
    visited[ix][iy] = True
    while queue:
        x, y, cnt = queue.popleft()
        cnt += 1
        max_value = max(max_value, cnt)
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if visited[nx][ny] or grid[nx][ny] == 'W': continue
            queue.append((nx, ny, cnt))
            visited[nx][ny] = True


R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
max_value = 0

for i in range(R):
    for j in range(C):
        if grid[i][j] == 'L':
            bfs(i, j)
            print(f'{i},{j}에서 시작할 때 경로 최대 = {max_value}')
print(max_value)