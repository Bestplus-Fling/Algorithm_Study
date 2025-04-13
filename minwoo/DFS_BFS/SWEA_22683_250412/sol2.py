import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


def bfs():
    global data, N, sx, sy, K, result
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque([(sx, sy, K, 0, 0)])
    visited = [[[[False] * N for _ in range(N)] for __ in range(K+1)] for ___ in range(4)]
    # visited = [[[False] * N for _ in range(N)] for __ in range(K+1)]
    visited[0][K][sx][sy] = True

    def is_valid(ix, iy, kk, dir, count):
        nonlocal queue, visited, dx, dy
        right = (dir + 1) % 4
        if not visited[right][kk][ix][iy]:
            queue.append((ix, iy, kk, right, count))
            visited[right][kk][ix][iy] = True
        left = (dir - 1) % 4
        if not visited[left][kk][ix][iy]:
            queue.append((ix, iy, kk, left, count))
            visited[left][kk][ix][iy] = True

    while queue:
        # print(queue)
        x, y, k, d, cnt = queue.popleft()
        if data[x][y] == 'Y':
            result = cnt
            return
        cnt += 1
        nx, ny = x + dx[d], y + dy[d]
        is_valid(x, y, k, d, cnt)
        if not(0 <= nx < N and 0 <= ny < N) or visited[d][k][nx][ny]:
            continue
        if data[nx][ny] == 'T':
            if k > 0:
                queue.append((nx, ny, k-1, d, cnt))
                visited[d][k-1][nx][ny] = True
        else:
            queue.append((nx, ny, k, d, cnt))
            visited[d][k][nx][ny] = True
            over = (d + 2) % 4
            queue.append((nx, ny, k, over, cnt+2))
            visited[over][k][nx][ny] = True


def define(data1):
    for i in range(N):
        for j in range(N):
            if data1[i][j] == 'X':
                return i, j


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    data = [list(input().strip()) for _ in range(N)]
    sx, sy = define(data)
    result = float('inf')
    bfs()
    print(f'#{tc}', result if result != float('inf') else -1)