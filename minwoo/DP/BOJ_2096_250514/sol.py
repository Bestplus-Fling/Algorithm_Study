import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
P = 3
prev_max = [0] * P
prev_min = [0] * P
dic = {0: (0, 2), 1: (0, 3), 2: (1, 3)}
for i in range(N):
    data = list(map(int, input().split()))
    next_max, next_min = [], []
    for j in range(P):
        s, e = dic[j]
        next_max.append(data[j] + max(prev_max[s:e]))
        next_min.append(data[j] + min(prev_min[s:e]))
    prev_min = [r for r in next_min]
    prev_max = [r for r in next_max]
print(max(prev_max), min(prev_min))
