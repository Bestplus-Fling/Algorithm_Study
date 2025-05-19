import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dxy = (1, 0), (0, 1), (-1, 0), (0, -1)


def bfs(x, y, color):
    global dxy, data, N, M, visited
    visited[x][y] = 1
    queue = deque([(x, y)])
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if color != data[nx][ny] or visited[nx][ny] == 1:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = 1
            cnt += 1
    return cnt


N, M = map(int, input().split())
data = [list(input().strip()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
white, blue = 0, 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == 1:
            continue
        n = bfs(i, j, data[i][j])
        if data[i][j] == 'W':
            white += n ** 2
        else:
            blue += n ** 2
print(white, blue)
