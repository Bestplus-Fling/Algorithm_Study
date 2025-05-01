import sys
sys.stdin = open('input.txt', 'r')
#########################################

'''

'''
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def check(dir, rotate):
    x, y = start_x, start_y
    cnt = 0
    while True:
        val = grid[x][y]
        if val > 0:
            l[val] = min(cnt,l[val])

        nx = x + dx[dir]
        ny = y + dy[dir]

        if not(0 <= nx <= n and 0 <= ny <= m):
            if rotate > 0:
                dir = (dir + 1)%4
            else:
                if dir != 0:
                    dir -= 1
                else:
                    dir = 3
        x = x + dx[dir]
        y = y + dy[dir]
        cnt += 1
        if x == start_x and y == start_y:
            return



m, n = map(int,input().split())
dic = {
    1: 0,
    2: n,
    3: 0,
    4: m
}
K = int(input())
grid = [[0] * (m + 1) for _ in range(n+1)]
l = [9999999999999999] * (K + 1)
for k in range(K + 1):
    a, b = map(int,input().split())
    if a < 3:
        i = dic[a]
        j = b
    else:
        i = b
        j = dic[a]
    if k != K:
        grid[i][j] = k + 1
    else:
        grid[i][j] = -1
        start_x , start_y = i, j

if a == 1:
    check(1, 1)
    check(3, -1)
elif a == 2:
    check(1, -1)
    check(3, 1)
elif a == 3:
    check(0, 1)
    check(2, -1)
else:
    check(0, -1)
    check(2, 1)

print(sum(l[1:]))




