import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


def BFS():
    global stf, stx, sty, building, R, C, L, result
    visited = [[[False] * C for _ in range(R)] for __ in range(L)]
    dkx = [1, 0, -1, 0]
    dky = [0, -1, 0, 1]
    queue = deque([[stf, stx, sty, 0]])
    visited[stf][stx][sty] = True
    while queue:
        f, x, y, cnt = queue.popleft()
        if building[f][x][y] == 'E':
            result = min(result, cnt)
            continue
        cnt += 1
        # 현재 층에서 아래 위로 인덱스가 있고, 그 곳이 빈칸일 경우도 queue에 추가
        next_f, prev_f = f + 1, f - 1
        if next_f < L and not visited[next_f][x][y]:
            if building[next_f][x][y] in ['.', 'E']:
                queue.append([next_f, x, y, cnt])
                visited[next_f][x][y] = True
        if prev_f >= 0 and not visited[prev_f][x][y]:
            if building[prev_f][x][y] in ['.', 'E']:
                queue.append([prev_f, x, y, cnt])
                visited[prev_f][x][y] = True
        for dx, dy in zip(dkx, dky):
            nx, ny = x + dx, y + dy
            if not(0 <= nx < R and 0 <= ny < C): continue
            if visited[f][nx][ny] or building[f][nx][ny] == '#': continue
            queue.append([f, nx, ny, cnt])
            visited[f][nx][ny] = True


while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        exit()
    # L은 층수
    # R과 C는 빌딩 한 층의 행과 열
    building = []
    stx, sty = -1, -1
    for ii in range(L):
        building.append([list(input().strip()) for _ in range(R)])
        temp = input()
        # print(*building[ii], sep='\n')
        # print()
        if (stx, sty) != (-1, -1): continue
        for i in range(R):
            for j in range(C):
                if building[ii][i][j] == 'S':
                    stf, stx, sty = ii, i, j
    result = float('inf')
    BFS()
    if result != float('inf'):
        print(f'Escaped in {result} minute(s).')
    else:
        print('Trapped!')
