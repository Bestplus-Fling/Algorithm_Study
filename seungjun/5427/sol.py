import sys
sys.stdin = open('input.txt', 'r')
######################################
from collections import deque


T = int(input())
for tc in range(1, T + 1):
    w, h = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    visited = [[-1] * w for _ in range(h)]
    can_go = 'IMPOSSIBLE'

    dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    queue = deque()
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '*':
                queue.append((i, j))
                visited[i][j] = 0

    while queue:
        i, j = queue.popleft()

        for dy, dx in dxy:
            ni, nj = i + dy, j + dx
            if ni < 0 or nj < 0 or h <= ni or w <= nj:
                continue
            if grid[ni][nj] == '#':
                continue
            if visited[ni][nj] != - 1 and visited[ni][nj] < visited[i][j] + 1:
                continue
            queue.append((ni, nj))
            visited[ni][nj] = visited[i][j] + 1

    # print(*visited, sep='\n')
    # print()

    for i in range(h):
        for j in range(w):
            if grid[i][j] == '@':
                queue.append((i, j))
                visited[i][j] = 0

    while queue:
        i, j = queue.popleft()

        for dy, dx in dxy:
            ni, nj = i + dy, j + dx
            if ni < 0 or nj < 0 or h <= ni or w <= nj:
                # 탈출시간 작성
                can_go = visited[i][j] + 1
                break
            if grid[ni][nj] == '#':
                continue
            if visited[ni][nj] != - 1 and visited[ni][nj] <= visited[i][j] + 1:
                continue
            queue.append((ni, nj))
            visited[ni][nj] = visited[i][j] + 1

    # print(*visited, sep='\n')

    print(can_go)