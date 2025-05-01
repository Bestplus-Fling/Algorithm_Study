import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
dxy = (1, 0), (0, 1), (0, -1), (-1, 0)


def delta():
    global grid, N, M, prefix
    queue = deque([(x2, y2)])
    prefix[x2][y2] = '0'
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if prefix[nx][ny] != '-1' or grid[nx][ny] == 0:
                continue
            queue.append((nx, ny))
            prefix[nx][ny] = str(1 + int(prefix[x][y]))


def check():
    global grid, N, M, prefix
    x, y = -1, -1
    for i in range(N):
        for ii in range(M):
            if grid[i][ii] == 2:
                x, y = i, ii
            elif grid[i][ii] == 0:
                prefix[i][ii] = '0'
    return x, y


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
prefix = [['-1'] * M for _ in range(N)]
x2, y2 = check()
delta()
for i in prefix:
    print(' '.join(i))
