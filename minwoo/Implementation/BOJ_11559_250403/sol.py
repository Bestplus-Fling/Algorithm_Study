import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def check():
    # 1. 바닥에 붙은 뿌요들의 방문 여부(visited 배열) 확인
    # 2. pang 함수를 호출하여 제거할 위치를 확인
    bomb = []
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '.' or visited[i][j]: continue
            temp = pang(i, j, visited)
            bomb.extend(temp)
    # 만약 터질게 하나도 없다면 종료
    if not bomb:
        return False
    # 터질게 하나라도 있다면, grid를 변경 (.으로)
    for x, y in bomb:
        grid[x][y] = '.'
    print(*grid, sep='\n')
    clean()
    return True


def pang(sx, sy, visited):
    # 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있다면(BFS)
    # 연결된 같은 색 뿌요들이 한꺼번에 없어진다.(1연쇄 시작)
    queue = deque([[sx, sy]])
    temp = [[sx, sy]]
    cnt = 1
    visited[sx][sy] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < M) or grid[nx][ny] == '.':
                continue
            if visited[nx][ny] or grid[sx][sy] != grid[nx][ny]:
                continue
            queue.append([nx, ny])
            temp.append([nx, ny])
            cnt += 1
            visited[nx][ny] = True
    if cnt >= 4:
        return temp
    return []


def clean():
    # 위에 다른 뿌요들이 있다면 중력에 의해 바닥으로 이동
    # 바닥에 붙어있는 뿌요들을 확인한다.
    # [row][col] 형태로 진행(위에서 아래로 내려가면서 스택에 append)
    # 스택에 하나라도 있으면 스택의 끝에서 바닥부터 채운다.
    for j in range(M):
        stack = []
        for i in range(N):
            if grid[i][j] != '.':
                stack.append(grid[i][j])
                grid[i][j] = '.'
        row = N-1
        while stack:
            puyo = stack.pop()
            grid[row][j] = puyo
            row -= 1


N, M = 12, 6
grid = [list(input().strip()) for _ in range(N)]
ans = 0
while True:
    if not check():
        break
    ans += 1
print(ans)


