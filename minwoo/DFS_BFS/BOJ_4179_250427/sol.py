import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dxy = (1, 0), (0, 1), (-1, 0), (0, -1)


def run_fire():
    global grid, fire, dxy
    temp = []
    for x, y in fire:
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if grid[nx][ny] in ['#', 'F']:
                continue
            grid[nx][ny] = 'F'
            temp.append((nx, ny))
    fire = temp


def bfs():
    global grid, R, C, dxy
    visited = [[0] * C for _ in range(R)]
    queue = deque([(stx, sty, 0)])
    visited[stx][sty] = 1
    time = -1
    while queue:
        x, y, t = queue.popleft()
        if x in [0, R-1] or y in [0, C-1]:
            return t + 1
        if t != time:
            run_fire()
            time += 1
        t += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if visited[nx][ny] or grid[nx][ny] in ['F', '#']:
                continue
            queue.append((nx, ny, t))
            visited[nx][ny] = 1
    return 'IMPOSSIBLE'


R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
fire = []
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'J':
            stx, sty = i, j
        elif grid[i][j] == 'F':
            fire.append((i, j))
print(bfs())