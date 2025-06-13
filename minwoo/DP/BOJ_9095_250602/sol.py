import sys
sys.stdin = open("input.txt", "r")
dp = [0] * 1000
dp[1], dp[2], dp[3] = 1, 2, 4


def f(n):
    for i in range(3, n+1):
        if dp[i] != 0: continue
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]


for t in range(int(input())):
    N = int(input())
    print(dp[N] if dp[N] != 0 else f(N))