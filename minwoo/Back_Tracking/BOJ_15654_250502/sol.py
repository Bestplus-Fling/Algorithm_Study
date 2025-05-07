import sys
sys.stdin = open("input.txt", "r")


def f(depth, nums, check):
    global ans, arr, N, M
    if depth == M:
        ans.append(' '.join(map(str, nums)))
        return
    for i in range(N):
        if check[i] == 1: continue
        check[i] = 1
        f(depth+1, nums+[arr[i]], check)
        check[i] = 0


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []
f(0, [], [0] * N)
print('\n'.join(map(str, ans)))
