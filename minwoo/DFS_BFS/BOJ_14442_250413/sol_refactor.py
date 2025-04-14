from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
dxy = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def bfs():
    global N, M, K, grid
    visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
    queue = deque([(0, 0, K, 1)])

    visited[0][0][K] = 1
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
            if grid[nx][ny] == 1 and z > 0 and visited[nx][ny][z-1] == 0:
                queue.append((nx, ny, z-1, cnt))
                visited[nx][ny][z-1] = 1
            # 벽 아닐때
            if grid[nx][ny] == 0 and visited[nx][ny][z] == 0:
                queue.append((nx, ny, z, cnt))
                visited[nx][ny][z] = 1
    return -1


N, M, K = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]
print(bfs())