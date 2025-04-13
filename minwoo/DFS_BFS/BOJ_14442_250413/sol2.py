from collections import deque
import sys
sys.stdin = open('input.txt', 'r')


def bfs():
    global N, M, K, grid
    dkx = [1, 0, -1, 0]
    dky = [0, 1, 0, -1]

    case = [(0, 0, K, 1)]
    visited = [[[False] * M for _ in range(N)] for __ in range(K + 1)]
    visited[K][0][0] = True
    i, _len = 0, 1
    while _len > i:
        x, y, k, cnt = case[i]
        if (x, y) == (N - 1, M - 1):
            return cnt
        cnt += 1
        for dx, dy in zip(dkx, dky):
            nx, ny = x + dx, y + dy
            if 0 > nx or N <= nx or 0 > ny or M <= ny:
                continue
            if grid[nx][ny] == '1' and k > 0 and not visited[k - 1][nx][ny]:
                case.append((nx, ny, k - 1, cnt))
                _len += 1
                visited[k - 1][nx][ny] = True
            if grid[nx][ny] == '0' and not visited[k][nx][ny]:
                case.append((nx, ny, k, cnt))
                _len += 1
                visited[k][nx][ny] = True
        i += 1
    return -1


N, M, K = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
print(bfs())
