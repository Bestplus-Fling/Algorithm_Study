import sys
sys.stdin = open('input.txt', 'r')

from collections import deque


def bfs():
    global data, N, M
    dxy = (1, 0), (0, 1)
    visited = [[0] * N for _ in range(M)]
    queue = deque([(0, 0)])
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        if x == M-1 and y == N-1:
            return 'Yes'
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == 1 or data[nx][ny] == 0:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = 1
    return 'No'


N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]
print(bfs())
