import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
dxy = (1, 0), (0, 1), (-1, 0), (0, -1)


def is_valid():
    global teacher, grid, dxy, N
    for x, y in teacher:
        for dx, dy in dxy:
            for k in range(N):
                nx, ny = x + dx*k, y + dy*k
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break
                if grid[nx][ny] == 'O':
                    break
                if grid[nx][ny] == 'S':
                    return False
    return True


def back(depth, row, col):
    global grid, N
    if depth == 3:
        if is_valid():
            print('YES')
            exit()
        return
    for r in range(row, N):
        for c in range(N):
            if r == row and c < col: continue
            if grid[r][c] in ['T', 'S', 'O']: continue
            grid[r][c] = 'O'
            back(depth+1, r, c)
            grid[r][c] = 'X'


N = int(input())
grid = [list(input().strip().split()) for _ in range(N)]
# print(*grid, sep='\n')
# 풍선팡 같은건가...?
teacher = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'T':
            teacher.append((i, j))
back(0, 0, 0)
print('NO')