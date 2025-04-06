import sys
sys.stdin = open('input.txt', 'r')


def change(start, end, increase):
    for i in range(start, end, increase):
        arr[i] = 'N' if arr[i] == 'Y' else 'Y'


arr = list(input().strip())
N = len(arr)
cnt = 0

for i in range(N):
    if arr[i] == 'Y':
        change(i, N, i+1)
        cnt += 1

print(cnt if N == arr.count("N") else -1)
