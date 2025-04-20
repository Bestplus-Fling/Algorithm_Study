import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def bfs():
    global N, M, K, grid
    dxy = (1, 0), (0, 1), (-1, 0), (0, -1)
    visited = [[[[False] * M for _ in range(N)] for __ in range(K+1)] for ___ in range(2)]
    queue = [(0, 0, K)]
    visited[0][K][0][0] = True
    cnt = 0
    day_night = 1
    while queue:
        temp = []
        cnt += 1
        day_night = 1 - day_night
        case = 4
        for x, y, z in queue:
            if x == N-1 and y == M-1:
                return cnt
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                # 벽 부수기는 day_night 가 0일때만 가능
                if day_night == 0:
                    if grid[nx][ny] == 1 and z > 0 and not visited[day_night][z-1][nx][ny]:
                        temp.append((nx, ny, z-1))
                        visited[day_night][z-1][nx][ny] = True
                    elif grid[nx][ny] == 0 and not visited[day_night][z][nx][ny]:
                        temp.append((nx, ny, z))
                        visited[day_night][z][nx][ny] = True
                else:
                    if grid[nx][ny] == 0 and not visited[day_night][z][nx][ny]:
                        temp.append((nx, ny, z))
                        visited[day_night][z][nx][ny] = True
                        case -= 1
            if case == 4:
                temp.append((x, y, z))
                visited[day_night][z][x][y] = True
        queue = temp
    return -1

N, M, K = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]
print(bfs())
