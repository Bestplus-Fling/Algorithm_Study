import sys
sys.stdin = open("input.txt", "r")

dp = [0] * 1009
dp[1] = 1
dp[2] = 2

"""
2 * n을 이루는 타일의 경우는 n-1에 1*2 타일, n-2에 dp[2]를 붙이는 경우
"""


def f(n):
    global dp
    if dp[n] != 0:
        return dp[n]
    for i in range(3, n+1):
        if dp[i] != 0: continue
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


N = int(input())
print(f(N) % 10007)
