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
                queue.append((i, j, 'fire'))
                visited[i][j] = 0

    for i in range(h):
        for j in range(w):
            if grid[i][j] == '@':
                queue.append((i, j, 'person'))
                visited[i][j] = 0

    while queue:
        # print(queue)
        i, j, type_ = queue.popleft()

        for dy, dx in dxy:
            ni, nj = i + dy, j + dx

            # 탈출 조건
            if type_ == 'person' and (ni < 0 or nj < 0 or ni >= h or nj >= w):
                can_go = visited[i][j] + 1
                # print(can_go)
                queue.clear()
                break
            if ni < 0 or nj < 0 or ni >= h or nj >= w:
                continue
            if visited[ni][nj] != -1:
                continue
            if grid[ni][nj] == '#':
                continue
            queue.append((ni, nj, type_))
            visited[ni][nj] = visited[i][j] + 1
        # print(queue)

    # print(*visited, sep='\n')

    print(can_go)