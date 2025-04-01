import sys
from collections import deque
sys.stdin = open("input.txt", "r")
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def bfs():
    grid = [r[:] for r in data]
    queue = deque(temp)
    c = 0
    while queue:
        x, y = queue.popleft()
        if result > zero - c:
            return -1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < M): continue
            if grid[nx][ny] >= 1: continue
            queue.append([nx, ny])
            grid[nx][ny] = 2
            c += 1
    return c


# 초기의 0 위치는 35개, 벽을 3개 설치하면 32개, 그중에서 중복되지 않고
# 설치할 수 있는 경우는
# 연구소에서 벽을 설치할 수 있는 공간의 개수를 측정
def case(depth):
    global result
    if depth == 3:
        c = bfs()
        if c != -1:
            result = max(result, zero - c)
        return
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                data[i][j] = 1
                case(depth + 1)
                data[i][j] = 0


N, M = map(int, input().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
temp = []
for di in range(N):
    for dj in range(M):
        if data[di][dj] == 2:
            temp.append([di, dj])
zero = -3
result = 0
for q in range(N):
    zero += data[q].count(0)
case(0)
print(result)
