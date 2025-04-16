import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
prefix = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        prefix[i][j] = data[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    base = prefix[x2][y2]
    dec1 = prefix[x2][y1-1]
    dec2 = prefix[x1-1][y2]
    inc = prefix[x1-1][y1-1]
    print(base - dec1 - dec2 + inc)
