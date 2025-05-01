import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


def f(ice, arr):
    global visited
    time = 0

    def is_valid(val, r, c):
        nonlocal ice, temp
        if val > 0:
            temp.append((r, c))
            return
        ice -= 1

    while True:
        # print(*grid, sep='\n', end='\n\n')
        temp = []
        visited = set()
        cnt = 0
        for x, y in arr:
            if (x, y) in visited:
                is_valid(grid[x][y], x, y)
                continue
            bfs([(x, y)])
            is_valid(grid[x][y], x, y)
            cnt += 1
            if cnt >= 2:    # cnt가 2 이상일 때 time을 return
                return time
        time += 1
        arr = temp
        if ice == 0:  # 얼음의 개수가 0이 되면 0 return
            return 0



def bfs(arr):
    global grid, N, M, visited
    dxy = (0, 1), (1, 0), (-1, 0), (0, -1)
    queue = deque(arr)
    visited.add(arr[0])
    while queue:
        x, y = queue.popleft()
        sea = 0
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if (nx, ny) in visited:   # 방문처리 확인
                continue

            if grid[nx][ny] == 0:    # 0이 저장된 칸의 개수를 확인, 감소시킨다.
                sea += 1
            else:
                queue.append((nx, ny))
                visited.add((nx, ny))
        grid[x][y] = grid[x][y] - sea
        if grid[x][y] <= 0:
            grid[x][y] = 0


N, M = map(int, input().split())
grid = [[int(i) for i in input().split()] for _ in range(N)]
check = []
count = 0
visited = set()
for i in range(N):
    for j in range(M):
        if grid[i][j] > 0:
            check.append((i, j))
            count += 1
print(f(count, check))
