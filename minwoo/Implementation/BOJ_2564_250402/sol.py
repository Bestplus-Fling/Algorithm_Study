import sys
sys.stdin = open('input1.txt', 'r')
###############
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def check(x, y, d, t):
    cnt = 0
    # print('시작')
    while True:
        # print(x, y)
        val = _map[x][y]
        if val > 0:
            # print(val, cnt)
            length[val-1] = min(length[val-1], cnt)

        nx, ny = x + dx[d], y + dy[d]
        if not(0 <= nx <= N and 0 <= ny <= M):
            if t > 0:
                d = (d + 1) % 4
            else:
                if d > 0:
                    d = d - 1
                else:
                    d = 3

        x, y = x + dx[d], y + dy[d]
        cnt += 1
        if x == start_x and y == start_y:
            return


M, N = map(int, input().split())
K = int(input())
dic = {1: 0, 2: N, 3: 0, 4: M}
_map = [[0] * (M+1) for _ in range(N+1)]
length = [99999999999] * K
for k in range(K+1):
    a, b = map(int, input().split())
    i, j = (dic[a], b) if a <= 2 else (b, dic[a])
    if k != K:
        _map[i][j] = k + 1
    else:
        start_x, start_y = i, j
        _map[i][j] = -1
# print(*_map, sep='\n')
if a == 1:
    check(start_x, start_y, 1, 1)
    check(start_x, start_y, 3, -1)
elif a == 2:
    check(start_x, start_y, 1, -1)
    check(start_x, start_y, 3, 1)
elif a == 3:
    check(start_x, start_y, 0, 1)
    check(start_x, start_y, 2, -1)
elif a == 4:
    check(start_x, start_y, 0, -1)
    check(start_x, start_y, 2, 1)
print(sum(length))
