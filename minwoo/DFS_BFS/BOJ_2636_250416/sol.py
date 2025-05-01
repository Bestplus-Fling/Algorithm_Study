import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
dxy = (1, 0), (0, 1), (-1, 0), (0, -1)


def bfs():
    global grid, R, C
    cnt = 0
    queue = deque([(0, 0)])
    visited = set()
    visited.add((0, 0))
    temp = []
    while queue:
        x, y = queue.popleft()
        if grid[x][y] == 1:
            temp.append((x, y))
            cnt += 1
            continue
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= R or ny < 0 or ny >= C or (nx, ny) in visited:
                continue
            queue.append((nx, ny))
            visited.add((nx, ny))
    for x, y in temp:
        grid[x][y] = 0
    return cnt


def count_cheese():
    global grid, R, C
    cnt = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                cnt += 1
    return cnt


R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
cheese, time = count_cheese(), 1
while True:
    decrease = bfs()
    if cheese - decrease == 0:
        break
    time += 1
    cheese -= decrease

print(time, cheese, sep='\n')

