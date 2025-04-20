import sys
sys.stdin = open('input.txt', 'r')


def color(x, y):
    global M, paper
    for i in range(y, y+M):
        for j in range(x, x+M):
            paper[i][j] = 1


def check():
    global paper, K
    dxy = (1, 0), (0, 1), (-1, 0), (0, -1)
    cnt = 0
    for i in range(K):
        for j in range(K):
            if paper[i][j] == 1:
                for di, dj in dxy:
                    ni, nj = i + di, j + dj
                    if not(0 <= ni < K and 0 <= nj < K):
                        continue
                    if paper[ni][nj] == 0:
                        cnt += 1
    return cnt


K = 102
M = 10
N = int(input())
paper = [[0] * K for _ in range(K)]
for _ in range(N):
    r, c = map(int, input().split())
    color(r, c)
print(check())
