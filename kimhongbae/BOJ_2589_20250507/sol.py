import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(i,j,arr):
    dxy = [[0,1],[1,0],[0,-1],[-1,0]]
    visited = [[0]*m for _ in range(n)]
    visited[i][j] = 1
    queue = deque([[i,j]])
    cnt = 0

    while queue:
        x,y = queue.popleft()
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if 0<= nx < n and 0<= ny <m:
                if visited[nx][ny]:continue
                if arr[nx][ny] == 'W':continue
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(cnt,visited[nx][ny])
                queue.append([nx,ny])
    return cnt-1

n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'W':continue
        result= max(result,bfs(i,j,arr))

print(result)