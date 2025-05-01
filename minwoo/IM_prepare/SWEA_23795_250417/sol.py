import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
dxy = (1, 0), (0, 1), (-1, 0), (0, -1)


def lazer(x, y):
    global data, N
    for dx, dy in dxy:
        for k in range(N):
            nx, ny = x + dx * k, y + dy * k
            if not(0 <= nx < N and 0 <= ny < N): break
            if data[nx][ny] == 1: break
            data[nx][ny] = 2


def search(n):
    global N, data
    cnt = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == n:
                if n == 2:
                    return i, j
                else:
                    cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    r, c = search(2)
    lazer(r, c)
    print(f'#{tc}', search(0))
