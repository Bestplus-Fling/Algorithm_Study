import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def f(hx, hy, ex, ey, MAP):
    dxy = (1, 0), (0, 1), (-1, 0), (0, -1)

    visited = [[[0] * 2 for _ in range(M)] for __ in range(N)]
    queue = deque([(hx, hy, 1, 0)])
    visited[hx][hy][1] = 1
    while queue:
        x, y, z, dp = queue.popleft()
        if (x, y) == (ex, ey):
            return dp
        dp += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if MAP[nx][ny] == 1 and z == 1 and visited[nx][ny][0] == 0:
                queue.append((nx, ny, 0, dp))
                visited[nx][ny][0] = 1
            elif MAP[nx][ny] == 0 and visited[nx][ny][z] == 0:
                queue.append((nx, ny, z, dp))
                visited[nx][ny][z] = 1
    return -1


N, M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())

print(f(Hx-1, Hy-1, Ex-1, Ey-1,
        [list(map(int, input().split())) for _ in range(N)]
        )
      )
