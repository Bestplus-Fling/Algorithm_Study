import sys
from collections import deque


def BFS():
    global N, M, grid, result
    dkx = [1, 0, -1, 0]
    dky = [0, 1, 0, -1]
    visited = [[[False] * M for _ in range(N)] for __ in range(2)]
    queue = deque([[0, 0, 1, 1]])
    visited[1][0][0] = True
    while queue:
        x, y, k, cnt = queue.popleft()
        if (x, y) == (N-1, M-1):
            result = min(result, cnt)
            continue
        cnt += 1
        for dx, dy in zip(dkx, dky):
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < M):
                continue
            if visited[k][nx][ny]: continue
            if grid[nx][ny] == '1':
                if k > 0:
                    queue.append([nx, ny, 0, cnt])
                    visited[0][nx][ny] = True
                continue
            queue.append([nx, ny, k, cnt])
            visited[k][nx][ny] = True


N, M = map(int, input().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
result = float('inf')
BFS()
print(result if result != float('inf') else -1)
