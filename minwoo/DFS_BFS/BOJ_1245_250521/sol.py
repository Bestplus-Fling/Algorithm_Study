import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
dxy = (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)


def bfs(x, y):
    global grid, N, M, visited, dxy
    q = deque([(x, y)])
    height = grid[x][y]
    is_peak = True
    # group = [(x, y)]
    # 1. 0이 아닌 칸 중에
    # 상하좌우 대각선에 있는 칸이 자신보다 낮은 칸
    # 그리고 같은 높이의 칸을 계속 탐색
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if grid[nx][ny] > height:
                is_peak = False
            if grid[nx][ny] == 0 or visited[nx][ny] == 1:
                continue
            if grid[nx][ny] == height:
                q.append((nx, ny))
                # group.append((nx, ny))
                visited[nx][ny] = 1
    return is_peak


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0 or visited[i][j] == 1:
            continue
        if bfs(i, j):
            result += 1
print(result)