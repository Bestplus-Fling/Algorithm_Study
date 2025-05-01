import sys
from collections import deque
input = sys.stdin.readline
dxy = (1, 0), (0, 1), (-1, 0), (0, -1)


def bfs(x, y):
    global grid, N, M
    queue = deque([(x, y)])
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        if grid[x][y] == 'P':
            cnt += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] or grid[nx][ny] == 'X':
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True
    if cnt == 0:
        return 'TT'
    return cnt


def start_point():
    global grid, N, M
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'I':
                return i, j


N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]
print(bfs(*start_point()))
