import sys
sys.stdin = open('input.txt', 'r')


def check(n):
    for x in range(N):
        for y in range(N):
            if n == data[x][y]:
                v[x][y] = 1
                binggo(x, y)
                return


def binggo(row, col):
    global cnt
    r_count = v[row].count(1)
    if r_count == N:
        cnt += 1
    c_count = 0
    for r in range(N):
        c_count += v[r][col]
    if c_count == N:
        cnt += 1
    dir1, dir2 = 0, 0

    for r in range(N):
        if not dir[0]:
            dir1 += v[r][r]
        if not dir[1]:
            dir2 += v[r][N-1-r]
    if dir1 == N:
        cnt += 1
        dir[0] = True
    if dir2 == N:
        cnt += 1
        dir[1] = True


N = 5
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
v = [[0] * N for _ in range(N)]
run = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt, ans = 0, 0
dir = [False] * 2
for i in run:
    for num in i:
        ans += 1
        check(num)
        if cnt >= 3:
            break
    else:
        continue
    break
print(ans)