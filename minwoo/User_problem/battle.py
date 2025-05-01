import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


def bfs():
    global grid, case, N, M
    dkx = [1, 0, -1, 0]
    dky = [0, -1, 0, 1]
    # visited = [[[False] * M for _ in range(N)] for __ in range(M1+MM)]
    visited = [[False] * M for _ in range(N)]
    queue = deque([(st_x, st_y, [])])
    visited[st_x][st_y] = True
    commend = ['D A', 'L A', 'U A', 'R A']
    while queue:
        x, y, cmd = queue.popleft()
        if (x, y) in case:
            return cmd, x, y
        for idx, dxy in enumerate(zip(dkx, dky)):
            dx, dy = dxy
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < M): continue
            if visited[nx][ny] or grid[nx][ny] in ['R', 'T', 'W']: continue
            cmd.append(commend[idx])
            queue.append((nx, ny, cmd[::]))
            visited[nx][ny] = True
            cmd.pop()


def define():
    global grid, N, M, case
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'A':
                sx, sy = i, j
            elif grid[i][j] == 'X':
                xx, xy = i, j
    # case.add((xx, xy))
    dir_check = [False] * 4
    for i in range(1, 3):
        for idx, dxy in enumerate(zip(dkx, dky)):
            # 나아가는 방향에 장애물이 있을 때 해당 방향 확인 x
            if dir_check[idx]: continue
            dx, dy = dxy
            nx, ny = xx + dx, xy + dy
            if not(0 <= nx < N and 0 <= ny < N): continue
            if grid[nx][ny] in ['R', 'T', 'W']:
                dir_check[idx] = True
                continue
            case.add((nx, ny))
    return sx, sy, xx, xy


def direction_valid(x, y, r, c):
    dx, dy = x-r, y-c
    dic = {1: 'D F', 2: 'U F', 3: 'R F', 4: 'L F'}
    if dx > 0:
        return dic[1]
    elif dx < 0:
        return dic[2]
    if dy > 0:
        return dic[3]
    elif dy < 0:
        return dic[4]


N, M, A, E, P = map(int, input().split())
grid = [list(input().split()) for _ in range(N)]

A1, Ah, R, M1, MM = input().split()
X1, XH = input().split()
case = set()
print(*grid, sep='\n')
st_x, st_y, en_x, en_y = define()
temp, ed_x, ed_y = bfs()
# print(ed_x, ed_y)
temp.append(direction_valid(en_x, en_y, ed_x, ed_y))
# print(temp)
print(' / '.join(temp))