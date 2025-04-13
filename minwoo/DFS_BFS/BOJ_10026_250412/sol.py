import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
dkx = [1, 0, -1, 0]
dky = [0, 1, 0, -1]


def traversal(data):
    global N
    visited = [[False] * N for _ in range(N)]

    def BFS(x, y, color):
        nonlocal visited, data
        queue = deque([(x, y)])
        visited[x][y] = True
        while queue:
            x, y = queue.popleft()
            for dx, dy in zip(dkx, dky):
                nx, ny = x + dx, y + dy
                if not(0 <= nx < N and 0 <= ny < N):
                    continue
                if visited[nx][ny]: continue
                if data[nx][ny] != color: continue
                queue.append((nx, ny))
                visited[nx][ny] = True
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                BFS(i, j, data[i][j])
                cnt += 1
    return cnt


def change_color():
    global data2
    for i in range(N):
        for j in range(N):
            if data2[i][j] == 'G':
                data2[i][j] = 'R'


N = int(input())
data1 = [list(input().strip()) for _ in range(N)]
data2 = [_[::] for _ in data1]
change_color()
print(traversal(data1), traversal(data2))
