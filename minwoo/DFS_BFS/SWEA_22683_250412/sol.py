import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
dkx = [-1, 0, 1, 0]
dky = [0, 1, 0, -1]
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# 최소 조작 회수
"""
목적지까지 이동시키기 위한 최소 조작 횟수
최대 2개의 나무를 밸 수 있다.
G: 이동 가능한 땅
T: 이동이 불가능한 나무
X: 현재 RC카 위치
Y: RC카를 이동시키고자 하는 위치

항상 위를 바라고보고 있다.(d = 0)
커멘드를 queue에 같이 삽입.
"""
dic1 = {
    0: [[-1, 0], [0, 1], [0, -1], [1, 0]],
    1: [[0, 1], [1, 0], [-1, 0], [0, -1]],
    3: [[0, -1], [1, 0], [-1, 0], [0, 1]],
    2: [[1, 0], [0, 1], [0, -1], [-1, 0]]
}

dic2 = {
    0: [0, 1, 3, 2],
    1: [1, 2, 0, 3],
    3: [3, 2, 0, 1],
    2: [2, 1, 3, 0]
}


def BFS(sx, sy):
    global checker, grid, B, result
    queue = deque([[sx, sy, B, 0, 0, []]])
    # queue = deque([[sx, sy, B, 0, 0]])
    visited[B][0][sx][sy] = True
    while queue:
        # print(queue)
        x, y, z, cnt, d, temp = queue.popleft()
        # x, y, z, cnt, d = queue.popleft()
        if cnt > result: continue
        cnt += 1
        temp.append([x, y])
        # for idx, dx, dy in enumerate(zip(dkx, dky)):
        for idx, dxy in enumerate(dic1[d]):
            dx, dy = dxy
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N): continue
            if idx == 0: k = 0
            elif idx < 3: k = 1
            else: k = 2
            if grid[nx][ny] == 'Y':
                print(temp)
                result = min(result, cnt+k)
                break
            if grid[nx][ny] == 'T':
                if z > 0 and not visited[z-1][dic2[d][idx]][nx][ny]:
                    queue.append([nx, ny, z-1, cnt+k, dic2[d][idx], temp[::]])
                    # queue.append([nx, ny, z-1, cnt+k, dir])
                    visited[z-1][dic2[d][idx]][nx][ny] = True
            else:
                if visited[z][dic2[d][idx]][nx][ny]: continue
                queue.append([nx, ny, z, cnt+k, dic2[d][idx], temp[::]])
                # queue.append([nx, ny, z, cnt+k, dir])
                visited[z][dic2[d][idx]][nx][ny] = True


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]
    checker = [[[[False] * N for _ in range(N)] for __ in range(4)] for ___ in range(B + 1)]
    # print(visited, sep='\n')
    # print(*grid, sep='\n')
    result = float('inf')
    start_x, start_y = -1, -1
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'X':
                start_x, start_y = i, j
    BFS(start_x, start_y)
    print(f'#{tc}', result if result != float('inf') else -1)
    for i in range(B):
        for j in range(4):
            print(*checker[i][j], sep='\n')
            print()
