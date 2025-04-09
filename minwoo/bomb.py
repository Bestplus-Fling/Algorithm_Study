import sys
sys.stdin = open("input1.txt", "r")
dkx = [1, 0, -1, 0]
dky = [0, 1, 0, -1]


def setting():
    global grid, next_bomb
    next_bomb = []
    for row in range(R):
        for col in range(C):
            if grid[row][col] == '.':
                next_bomb.append((row, col))
                grid[row][col] = 'O'


def bomb():
    global grid, next_bomb, now_bomb
    while now_bomb:
        x, y = now_bomb.pop()
        grid[x][y] = '.'
        for dx, dy in zip(dkx, dky):
            nx, ny = x + dx, y + dy
            if not(0 <= nx < R and 0 <= ny < C): continue
            grid[nx][ny] = '.'
    for x, y in next_bomb:
        if grid[x][y] == 'O':
            now_bomb.append((x, y))


R, C, N = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
next_bomb, now_bomb = [], []
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'O':
            now_bomb.append((i, j))

if N != 1:
    mod = N % 16
    idx = 1
    while idx != mod:
        if (idx % 4) % 2 == 0:
            setting()
        else:
            bomb()
        print(*grid, sep='\n')
        print(now_bomb, end='\n\n')
        idx = (idx + 1) % 16
for g in grid:
    print(''.join(g))
