import sys
sys.stdin = open('input.txt', 'r')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def is_valid(commends):
    global sx, sy, grid, N
    x, y = sx, sy
    d = 0
    for cmd in commends:
        if cmd == 'R':
            d = (d + 1) % 4
        elif cmd == 'L':
            d = (d - 1) % 4
        else:
            nx, ny = x + dx[d], y + dy[d]
            if not(0 <= nx < N and 0 <= ny < N): continue
            if grid[nx][ny] == 'T': continue
            x, y = nx, ny
    if grid[x][y] == 'Y':
        return 1
    return 0


def check():
    global grid
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'X':
                return i, j


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]
    sx, sy = check()
    result = []
    Q = int(input())
    for q in range(Q):
        C, commend = input().split()
        commend = list(commend.strip())
        result.append(is_valid(commend))
    print(f'#{tc}', *result)