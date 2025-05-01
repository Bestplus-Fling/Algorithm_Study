import sys
sys.stdin = open('input.txt', 'r')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
note = list(input().strip())
# 첫 방향은 아래를 바라본다.
# idx 순서는 위 0, 오른쪽 1, 아래 2, 왼쪽 3
# R이라면 idx += 1 / L은 idx -= 1
# F는 한칸 전진
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
# print(location)
sort_x = sorted(location, key=lambda k: k[0])
sort_y = sorted(location, key=lambda k: k[1])

min_x  = sort_x[0][0]
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
