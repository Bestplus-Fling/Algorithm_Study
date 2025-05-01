import sys
sys.stdin = open('input.txt', 'r')


def f():
    global N, M, data
    dxy = (1, 0), (0, 1), (-1, 0), (0, -1)
    bxy = (1, 1), (1, -1), (-1, 1), (-1, -1)
    result = 0
    for x in range(N):
        for y in range(N):
            case1 = data[x][y]
            case2 = data[x][y]
            for k in range(1, M):
                for dx, dy in dxy:
                    nx, ny = x + dx*k, y + dy*k
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    case1 += data[nx][ny]
                for bx, by in bxy:
                    nx, ny = x + bx * k, y + by * k
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    case2 += data[nx][ny]
            result = max(result, case1, case2)
    return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', f())
