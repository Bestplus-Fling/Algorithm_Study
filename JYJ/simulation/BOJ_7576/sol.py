import sys
sys.stdin = open('input.txt', 'r')
#########################################
import sys
from collections import deque
input = sys.stdin.readline
'''

'''

dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def bfs():
    queue = deque()
    depth = 0
    for i in range(n): # 토마토 한개인줄 알았는데 아님;;
        for j in range(m):
            if arr[i][j] == 1:
                queue.append((i, j, 0))
    while queue:
        i, j, depth = queue.popleft()
        for dx, dy in dxy:
            ni = i + dx
            nj = j + dy

            if not(0 <= ni < n and 0 <= nj < m) or arr[ni][nj] == -1 or arr[ni][nj] == 1: continue

            arr[ni][nj] = 1
            queue.append((ni, nj, depth + 1))

    return depth


m, n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

result = bfs()

for i in range(n): # 익지 않은 토마토(0)이 있다면 -1 출력
    for j in range(m):
        if arr[i][j] == 0:
            result = -1
            break
    if result == -1:
        break

print(result)






