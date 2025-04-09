import sys
sys.stdin = open('input.txt', 'r')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
data = list(input().strip())

d = 2
x, y = 0, 0
location = [[x, y]]
for i in range(N):
    if data[i] == 'L':  # -1
        d = (d - 1) if d > 0 else 3
    elif data[i] == 'R': # +1
        d = (d + 1) % 4
    else:   # 전진
        x, y = x + dx[d], y + dy[d]
        location.append([x, y])
# print(location)
sort_x = sorted(location, key=lambda k: k[0])
sort_y = sorted(location, key=lambda k: k[1])

min_x = sort_x[0][0]
min_y = sort_y[0][1]
cnt = len(location)
if min_x < 0:
    abs_x = abs(min_x)
    for i in range(cnt):
        location[i][0] += abs_x
if min_y < 0:
    abs_y = abs(min_y)
    for i in range(cnt):
        location[i][1] += abs_y
R, C = sort_x[-1][0] + 1, sort_y[-1][1] + 1
grid = [['#'] * C for _ in range(R)]
for x, y in location:
    grid[x][y] = '.'
for row in grid:
    print(''.join(row))
