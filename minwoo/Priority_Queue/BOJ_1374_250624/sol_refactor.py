import sys
import heapq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
classes = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])

hq = []
res = 0

for _, start, end in classes:
    while hq and hq[0] <= start:
        heapq.heappop(hq)
    heapq.heappush(hq, end)
    res = max(res, len(hq))
print(res)