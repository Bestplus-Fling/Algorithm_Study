import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
villain = 0
for i in range(N):
    villain += arr[i][1]
cnt = 0
for i in range(N):
    cnt += arr[i][1]
    if cnt >= villain/2:
        print(arr[i][0])
        break

