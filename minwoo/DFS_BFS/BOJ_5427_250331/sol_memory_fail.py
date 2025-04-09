import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
#########################################
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def burn():
    global fire
    temp = []
    while fire:
        x, y = fire.pop()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < H and 0 <= ny < W): continue
            if data[nx][ny] == '#': continue
            data[nx][ny] = '*'
            temp.append([nx, ny])
    fire.extend(temp)


def BFS(x, y):
    queue = deque([[x, y, 1]])
    visited = [[False] * W for _ in range(H)]
    visited[x][y] = True
    check = 0
    while queue:
        x, y, depth = queue.popleft()
        # 리스트 범위 밖으로 벗어나는 경우
        if check != depth:
            burn()
            check += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < H and 0 <= ny < W):
                return depth
            if data[nx][ny] != '.' or visited[nx][ny]:
                continue
            queue.append([nx, ny, depth+1])
            visited[nx][ny] = True
    return -1


for tc in range(int(input())):
    W, H = map(int, sys.stdin.readline().split())
    data = [list(sys.stdin.readline().strip()) for _ in range(H)]
    fire, result = [], 0
    # 상근이 시작 위치 @, 불 위치 *
    for i in range(H):
        for j in range(W):
            if data[i][j] == '@':
                si, sj = i, j
            elif data[i][j] == '*':
                fire.append([i, j])
    result = BFS(si, sj)
    print(result if result != -1 else 'IMPOSSIBLE')
