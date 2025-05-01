import sys
sys.stdin = open('input1.txt', 'r')
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def move():
    global stack, data
    temp = []
    for row, col in stack:
        if data[row][col] == '.': continue
        x, y = row, col
        s, d, size = data[row][col]
        data[row][col] = '.'
        for q in range(s):
            if not(0 <= x + dx[d] < R and 0 <= y + dy[d] < C):
                if d < 2:
                    d = 0 if d else 1
                else:
                    d = 2 if d == 3 else 3
            x, y = x + dx[d], y + dy[d]
        temp.append([x, y, s, d, size])
    grid = []
    for assm in temp:
        if data[assm[0]][assm[1]] != '.' and data[assm[0]][assm[1]][2] > assm[4]:
            continue
        data[assm[0]][assm[1]] = (assm[2], assm[3], assm[4])
        grid.append((assm[0], assm[1]))
    stack = grid


R, C, M = map(int, sys.stdin.readline().split())
data = [['.'] * C for _ in range(R)]
stack = []
for i in range(M):
    r, c, speed, direction, z = map(int, sys.stdin.readline().split())
    data[r-1][c-1] = (speed, direction-1, z)
    stack.append((r-1, c-1))
K = 0
for j in range(C):
    for i in range(R):
        if data[i][j] == '.': continue
        K += data[i][j][2]
        data[i][j] = '.'
        break
    move()
print(K)
