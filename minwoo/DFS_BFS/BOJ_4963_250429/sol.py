import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def bfs(x, y):
    global visited, land, w, h
    dxy = (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)
    queue = deque([(x, y)])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if visited[nx][ny] == 1 or land[nx][ny] == 0:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = 1


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    land = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 1 or land[i][j] == 0: continue
            bfs(i, j)
            ans += 1
    print(ans)
