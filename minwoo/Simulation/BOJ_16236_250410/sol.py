import sys
sys.stdin = open('input.txt', 'r')

# N * N 크기의 공간에 물고기 M 마리와 아기 상어 1마리
# 한 칸에 물고기 최대 1마리

# 아기상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고
# 나머지 칸은 모두 지나갈 수 있다.
# 아기 상어의 이동은 1초,
# 물고기를 먹는데 걸리는 시간은 없음(이동과 동시에 다음 물고기 탐색)
# 이동과 동시에 물고기를 먹고, 그 칸은 빈칸
# 아기 상어는 자신의 크기가 같은 수의 물고기를 먹을때마다 크기가 1 증가
from collections import deque
dkx = [-1, 0, 0, 1]
dky = [0, -1, 1, 0]


def fish_count():
    # 자기보다 작은 물고기만 먹을 수 있다(초기 크기 2)
    global location, grid, now_x, now_y, size
    temp = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 9:
                now_x, now_y = i, j
            elif 0 < grid[i][j] < size:
                temp += 1
                location.add((i, j))
    return temp


def BFS(sx, sy):
    global location, N, size
    visited = [[False] * N for _ in range(N)]
    # 무조건 갱신 아니고, 먹이에 도달했을 때, Flag -> False
    # 동일한 범위에 있는 먹이들만 검증하는 것,
    queue = deque([[sx, sy, 0]])
    visited[sx][sy] = True
    temp = []
    grid[sx][sy] = 0
    while queue:
        x, y, t = queue.popleft()
        t += 1
        for dx, dy in zip(dkx, dky):
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < N) or visited[nx][ny]: continue
            if grid[nx][ny] > size: continue
            if (nx, ny) in location and grid[nx][ny] != 0:
                temp.append([nx, ny, t])
            queue.append([nx, ny, t])
            visited[nx][ny] = True
    if not temp:
        return 0, sx, sy
    print(temp)
    x, y, t = sorted(temp, key=lambda b: (b[2], b[0], b[1]))[0]
    location.discard((x, y))
    grid[x][y] = 9
    return t, x, y


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

size, time = 1, 0
eat_count = 1
location = set()
now_x, now_y = -1, -1
# 더 이상 먹을 수 있는 물고기가 공간에 없다면, 아기 상어는 엄마 상어에게 도움을 요청
while True:
    if eat_count == size:
        size += 1
        eat_count = 0
        location = set()
        fish = fish_count()
    print(*grid, sep='\n')
    print(f'(({time}s, Lv:{size}, Exp:{eat_count} / {size}))')
    print(location)
    print()
    if fish == 0:
        break
    else:
        """
        - 먹을 수 있는 물고기가 1마리보다 많다면, 
            거리가 가장 가까운 물고기를 먹으러 간다
            - 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때,
                지나가야 하는 칸의 개수의 최소값
            - 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기,
                그러한 물고기가 여러 마리라면, 가장 왼쪽에 있는 물고기
        """
        tk, now_x, now_y = BFS(now_x, now_y)
        if tk == 0:
            break
        time += tk
        eat_count += 1
        fish -= 1
print(time)
