import sys
sys.stdin = open("input.txt", "r")

"""
1. x가 3으로 나누어 떨어지면 3으로 나눈다
2. x가 2로 나누어 떨어지면 2로 나눈다
3. 1을 뺀다
3개의 연산을 적절히 사용해서 1을 만드려고 한다.
"""
dp = [0] * ((10 ** 6) + 1)
N = int(input())

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[N])
