import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def bfs():
    global N, M, K, grid
    dxy = (1, 0), (0, 1), (-1, 0), (0, -1)
    visited = [[[0] * M for _ in range(N)] for __ in range(K+1)]
    queue = [(0, 0, K)]
    visited[K][0][0] = 1
    day_night = 1
    cnt = 0
    while queue:
        temp = []
        day_night = 1 - day_night
        cnt += 1
        for x, y, z in queue:
            if x == N-1 and y == M-1:
                return cnt
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if grid[nx][ny] == 1 and z > 0 and visited[z-1][nx][ny] == 0:
                    if day_night == 0:
                        temp.append((nx, ny, z-1))
                        visited[z-1][nx][ny] = 1
                    else:
                        temp.append((x, y, z))
                elif grid[nx][ny] == 0 and visited[z][nx][ny] == 0:
                    temp.append((nx, ny, z))
                    visited[z][nx][ny] = 1
        queue = temp
    return -1


N, M, K = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]
print(bfs())
