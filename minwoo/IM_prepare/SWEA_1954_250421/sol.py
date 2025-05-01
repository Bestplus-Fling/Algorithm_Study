import sys
sys.stdin = open('input.txt', 'r')


def snail(num):
    global arr
    dir = 1
    k = 1
    x, y = 0, -1
    while True:
        for i in range(num):
            y += dir
            arr[x][y] = k
            k += 1
        num -= 1
        if num == 0:
            return
        for j in range(num):
            x += dir
            arr[x][y] = k
            k += 1
        dir *= -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stop_point = []
    arr = [[0] * N for _ in range(N)]
    snail(N)
    print(f'#{tc}')
    for a in arr:
        print(*a)
