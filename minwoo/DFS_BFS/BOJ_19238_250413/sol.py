import sys
sys.stdin = open('input1.txt', 'r')
from collections import deque


def bfs():
    global grid, checker, arrival, N
    queue = deque([(st_x, st_y)])
    visited = [[False] * N for _ in range(N)]
    visited[st_x][st_y] = True
    temp = []
    while queue:
        x, y = queue.popleft()
        if grid[x][y]:
            temp.append((x, y))
        if temp: continue
        # 같은 최단거리에 있는 승객의 경우
        # 행번호가 작은 손님
        # 행 번호가 같다면 열 번호가 가장 작은 손님
        # 손님을 만나면 바로 종료가 아니라, 승객이 있는 좌표를 저장
        # 정렬 후 가장 앞에 있는 승객좌표로 이동
        pass


def passenger(m):
    global grid, arrival
    for i in range(2, m+2):
        x, y, r, c = map(int, input().split())
        grid[x-1][y-1] = i
        arrival.append([r-1, c-1])


N, M, F = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
st_x, st_y = map(int, input().split())
arrival = []
checker = [False] * M
passenger(M)
print(arrival)
print(*grid, sep='\n')
