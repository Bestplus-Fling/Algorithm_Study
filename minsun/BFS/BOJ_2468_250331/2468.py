import sys
from importlib.util import find_spec
from collections import deque

sys.stdin = open("input.txt")

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def safe_place(start_x, start_y, h):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:

            nx = dx + x
            ny = dy + y

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] != 1:
                if zido[nx][ny] > h and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))



N = int(input())
zido = [list(map(int, input().split())) for _ in range(N)]

max_height = max(max(x) for x in zido)
result = []

for h in range(0, max_height + 1):
    visited = [[0]*N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if zido[i][j] > h and not visited[i][j]:
                safe_place(i, j, h)
                count += 1

    result.append(count)

print(max(result))