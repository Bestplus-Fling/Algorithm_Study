import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
#########################################
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def burn(temp):
    f = deque(temp)
    for x, y, t in f:
        grid[x][y] = 0
    while f:
        x, y, depth = f.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < H and 0 <= ny < W): continue
            if data[nx][ny] == '#': continue
            if grid[nx][ny] > -1: continue
            grid[nx][ny] = depth
            f.append([nx, ny, depth+1])


def BFS(x, y):
    queue = deque([[x, y, 0]])
    while queue:
        x, y, depth = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < H and 0 <= ny < W):
                return depth+1
            if 0 <= grid[nx][ny] <= depth+1:
                continue
            if data[nx][ny] in ['#', '@', '*']:
                continue
            queue.append([nx, ny, depth+1])
            data[nx][ny] = '@'
    return -1


for tc in range(int(input())):
    W, H = map(int, sys.stdin.readline().split())
    data = [list(sys.stdin.readline().strip()) for _ in range(H)]
    fire, result = [], 0
    grid = [[-1] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if data[i][j] == '@':
                si, sj = i, j
            elif data[i][j] == '*':
                fire.append([i, j, 1])
    burn(fire)
    print(*grid, sep='\n')
    result = BFS(si, sj)
    print(result if result != -1 else 'IMPOSSIBLE')
    print(*data, sep='\n')
