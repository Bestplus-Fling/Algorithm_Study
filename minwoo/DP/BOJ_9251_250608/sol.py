import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

A = input().strip()
B = input().strip()
x, y = len(A) + 1, len(B) + 1
dp = [[0] * y for _ in range(x)]
for i in range(1, x):
    for j in range(1, y):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])
