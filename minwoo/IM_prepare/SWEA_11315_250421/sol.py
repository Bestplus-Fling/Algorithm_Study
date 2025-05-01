import sys
sys.stdin = open('input.txt', 'r')


def is_valid():
    global grid, N
    dxy = (1, 0), (0, 1), (1, 1), (1, -1)
    for x in range(N):
        for y in range(N):
            if grid[x][y] == '.': continue
            for dx, dy in dxy:
                cnt = 1
                k = 1
                while True:
                    nx, ny = x + dx * k, y + dy * k
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        break
                    if grid[nx][ny] == '.':
                        break
                    cnt += 1
                    if cnt >= 5:
                        return 'YES'
                    k += 1
    return 'NO'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]
    print(f'#{tc}', is_valid())
