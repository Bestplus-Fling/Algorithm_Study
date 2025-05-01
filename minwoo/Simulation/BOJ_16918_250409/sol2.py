import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
dkx = (1, 0, -1, 0)
dky = (0, 1, 0, -1)


def delta():
    global grid, bomb, next_bomb
    while bomb:
        x, y = bomb.popleft()
        grid[x][y] = '.'
        for dx, dy in zip(dkx, dky):
            nx, ny = x + dx, y + dy
            if not(0 <= nx < R and 0 <= ny < C):
                continue
            grid[nx][ny] = '.'
    bomb = deque(next_bomb)
    next_bomb = []


def set_bomb():
    global bomb, grid, next_bomb
    for row in range(R):
        for col in range(C):
            if grid[row][col] == '.':
                next_bomb.append((row, col))
                grid[row][col] = 'O'


R, C, N = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
bomb = deque()
next_bomb = []
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'O':
            bomb.append((i, j))
mod = N % 10
idx = 1
while idx != N:
    print(*grid, sep='\n', end='\n\n')
    print(bomb)
    # if idx % 4 in [1, 3]:
    #     set_bomb()
    if idx in [1, 3]:
        set_bomb()
    else:
        delta()
    # idx = (idx + 1) % 10
    idx += 1

for g in grid:
    print(''.join(g))
