import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
dxy = (1, 0), (0, 1), (-1, 0), (0, -1)


def change_air():
    global data, N, M
    visited = [[0] * M for _ in range(N)]
    queue = deque([(0, 0)])
    visited[0][0] = 1
    data[0][0] = 2
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] == 1:
                continue
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                queue.append((nx, ny))
                visited[nx][ny] = 1


def cut_cheese():
    global data, N, M
    cnt = 0
    outside = []
    visited = [[0] * M for _ in range(N)]
    queue = deque([(0, 0)])
    visited[0][0] = 1
    # 테두리에 있는 치즈만 확인
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] == 1:
                continue
            if data[nx][ny] == 2:
                queue.append((nx, ny))
            elif data[nx][ny] == 1:
                outside.append((nx, ny))
            else:
                data[nx][ny] = 2
                queue.append((nx, ny))
            visited[nx][ny] = 1
    for x, y in check_blank(outside):
        data[x][y] = 0
        cnt += 1
    return cnt


def check_blank(check_list):
    global data, dxy
    delete = []
    for x, y in check_list:
        c = 0
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if data[nx][ny] == 2:
                c += 1
        if c >= 2:
            delete.append((x, y))
    return delete


N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
cheese = 0
for i in range(N):
    for j in range(M):
        if data[i][j] != 0:
            cheese += 1
change_air()
time, delete_ch = 0, []
while cheese:
    time += 1
    cheese -= cut_cheese()
print(time)
