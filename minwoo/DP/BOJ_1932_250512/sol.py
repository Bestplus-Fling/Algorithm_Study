import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def f():
    global data, N, result, dp
    for i in range(N):
        for j in range(i+1):
            # print(f'{data[i][j]}는 {dp[i][j]}와 {dp[i][j+1]} 중 하나를 선택')
            dp[i+1][j+1] = max(dp[i][j+1] + data[i][j], dp[i][j] + data[i][j])


N = int(input())
dp = [[0] * (N+1) for _ in range(N+1)]
data = [list(map(int, input().split())) for _ in range(N)]
result = 0
f()
print(max(dp[-1]))

