from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
dxy = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def bfs():
    global N, M, K, grid
    visited = [[[False] * M for _ in range(N)] for _ in range(K+1)]
    queue = deque([(0, 0, K, 1)])
    for k in range(K+1):
        visited[k][0][0] = True
    while queue:
        x, y, z, cnt = queue.popleft()
        if x == N-1 and y == M-1:
            return cnt
        cnt += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            # 방문처리
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽일때
            if grid[nx][ny] == '1' and z > 0 and not visited[z-1][nx][ny]:
                queue.append((nx, ny, z-1, cnt))
                visited[z-1][nx][ny] = True
            # 벽 아닐때
            if grid[nx][ny] == '0' and not visited[z][nx][ny]:
                queue.append((nx, ny, z, cnt))
                visited[z][nx][ny] = True
    return -1


N, M, K = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
print(bfs())