import sys
sys.stdin = open('input.txt', 'r')
######################################
from collections import deque


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

h = -1

for i in range(n):
    for j in range(n):
        if h < arr[i][j]:
            h = arr[i][j]

max_cnt = -float('inf')
queue = deque()
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for k in range(h):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            if arr[i][j] - k <= 0:
                continue
            cnt += 1
            queue.append((i, j))
            visited[i][j] = True

            while queue:
                idx, jdx = queue.popleft()

                for dy, dx in dxy:
                    ni, nj = idx + dy, jdx + dx
                    if ni < 0 or nj < 0 or n <= ni or n <= nj:
                        continue
                    if visited[ni][nj]:
                        continue
                    if arr[ni][nj] - k <= 0:
                        continue
                    queue.append((ni, nj))
                    visited[ni][nj] = True

    max_cnt = max(max_cnt, cnt)

print(max_cnt)