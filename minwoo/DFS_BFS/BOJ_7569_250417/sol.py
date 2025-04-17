import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque
dxy = (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)


def bfs(st):
    global tomato, N, M, H, visited, dxy
    queue = deque(st)
    cnt = 0
    time = 1
    while queue:
        x, y, z = queue.popleft()
        time = visited[x][y][z]
        cnt += 1
        for dx, dy, dz in dxy:
            nx, ny, nz = x + dx, y + dy, z + dz
            if not(0 <= nx < N and 0 <= ny < M and 0 <= nz < H):
                continue
            if visited[nx][ny][nz]: continue
            if tomato[nz][nx][ny] in [-1, 1]: continue
            queue.append((nx, ny, nz))
            visited[nx][ny][nz] = 1 + visited[x][y][z]
    return cnt, time-1


M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]
start = []
tomato_count = 0
visited = [[[0] * H for ____ in range(M)] for ___ in range(N)]
for k in range(H):
    for r in range(N):
        for c in range(M):
            if tomato[k][r][c] == 1:
                start.append((r, c, k))
                visited[r][c][k] = 1
                tomato_count += 1
            elif tomato[k][r][c] == 0:
                tomato_count += 1

check, pp = bfs(start)
print(pp if tomato_count - check == 0 else -1)

