import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    queue = deque([(j, i) for i, j in enumerate(list(map(int, input().split())))])
    cnt = 1
    while queue:
        temp = queue.popleft()
        max_val = 0
        for i, j in queue:
            max_val = max(max_val, i)
        if temp[0] < max_val:
            queue.append(temp)
            continue
        if temp[1] == M:
            print(cnt)
            break
        cnt += 1
