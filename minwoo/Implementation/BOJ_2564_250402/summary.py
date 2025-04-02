import sys
sys.stdin = open('input.txt', 'r')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def check(direction, rotate):
    x, y = start_x, start_y
    cnt = 0
    while True:
        val = grid[x][y]
        if val > 0:
            length[val] = min(cnt, length[val])
        # 마지막에 좌표를 갱신하고 나서 조건으로 사용
        nx = x + dx[direction]
        ny = y + dy[direction]
        if not(0 <= nx <= N and 0 <= ny <= M):
            if rotate > 0:
                direction = (direction+1) % 4
            else:
                if direction != 0:
                    direction -= 1
                else:
                    direction = 3
        x = x + dx[direction]
        y = y + dy[direction]
        cnt += 1
        if x == start_x and y == start_y:
            return


M, N = map(int, input().split())
dic = {
    1: 0,
    2: N,
    3: 0,
    4: M,
}
K = int(input())
grid = [[0] * (M+1) for _ in range(N+1)]
length = [9999999999] * (K+1)
for k in range(K+1):
    a, b = map(int, input().split())
    if a < 3:
        i = dic[a]
        j = b
    else:
        i = b
        j = dic[a]
    if k != K:
        grid[i][j] = k+1
    else:
        grid[i][j] = -1
        start_x, start_y = i, j
# print(*grid, sep='\n')
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
print(sum(length[1::]))
