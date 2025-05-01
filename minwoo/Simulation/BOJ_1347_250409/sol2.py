import sys
sys.stdin = open('input.txt', 'r')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
note = list(input().strip())
dir = 2
x, y = 0, 0
location = [[x, y]]
for i in range(N):
    if note[i] == "L":  # -1
        dir = (dir - 1) if dir > 0 else 3
    elif note[i] == "R": # +1
        dir = (dir + 1) % 4
    else:   # 좌표 이동
        x, y = x + dx[dir], y + dy[dir]
        location.append([x, y])

sort_x = sorted(location, key=lambda k: k[0])
sort_y = sorted(location, key=lambda k: k[1])

min_x = sort_x[0][0]
min_y = sort_y[0][1]
if min_x < 0:
    abs_x = abs(min_x)
    for loc in location:
        loc[0] += abs_x
if min_y < 0:
    abs_y = abs(min_y)
    for loc in location:
        loc[1] += abs_y
R, C = sort_x[-1][0] + 1, sort_y[-1][1] + 1

grid = [['#'] * C for _ in range(R)]

for x, y in location:
    grid[x][y] = '.'
for g in grid:
    print(''.join(g))