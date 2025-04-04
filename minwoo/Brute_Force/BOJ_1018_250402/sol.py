import sys
sys.stdin = open("input7.txt", "r")


def change(sx, sy, ex, ey, c, data):
    cnt = 0
    for ii in range(sx, ex):
        for jj in range(sy, ey):
            if data[ii][jj] != c:
                cnt += 1
            c = 'B' if c != 'B' else 'W'
        c = 'B' if c != 'B' else 'W'
    return cnt


def check(sx, sy, data):
    global ans, visited
    ex, ey = sx + 8, sy + 8
    if ex >= N:
        sx, ex = N-8, N
    if ey >= M:
        sy, ey = M - 8, M
    if (sx, sy) in visited: return
    # print(f'{sx}에서 {ex-1}까지, {sy}에서 {ey-1}까지')

    cnt1 = change(sx, sy, ex, ey, 'B', data)
    cnt2 = change(sx, sy, ex, ey, 'W', data)
    cnt = min(cnt1, cnt2)
    ans = min(cnt, ans)
    visited.add((sx, sy))


N, M = map(int, input().split())
data = [list(input().strip()) for _ in range(N)]

ans = float('inf')
visited = set()
for i in range(N):
    for j in range(M):
        check(i, j, data)
# print(*data, sep='\n')
print(ans)
