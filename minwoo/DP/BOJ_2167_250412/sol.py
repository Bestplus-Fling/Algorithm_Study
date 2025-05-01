import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
K = int(input())
for k in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    value = 0
    for ix in range(i-1, x):
        for jy in range(j-1, y):
            value += arr[ix][jy]
    print(value)