import sys
sys.stdin = open('input.txt', 'r')
dp = [0] * 100
num = [tuple()] * 100
dp[1] = 1
num[0] = (1, 0)
num[1] = (0, 1)
idx = 2


def fibo(n):
    global dp, num, idx
    if n == 0:
        return num[n]
    elif n == 1:
        return num[n]
    for i in range(idx, n+1):
        zero, one = 0, 0
        dp[i] = dp[i-1] + dp[i-2]
        idx += 1
        for j in range(i-2, i):
            x, y = num[j]
            zero += x
            one += y
        num[i] = (zero, one)
    return num[n]


for t in range(int(input())):
    print(*fibo(int(input())))
