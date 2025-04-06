import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

result = [0]*N


for i in range(N):
    x = arr[i]
    xx = i - x
    for j in range(i, xx, -1):
        result[j] = result[j - 1]
    result[xx] = i + 1

print(*result)

