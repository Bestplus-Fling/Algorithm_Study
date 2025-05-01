import sys
from collections import deque
sys.stdin = open("input3.txt", "r")
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def bfs():
    # 깊은 복사로 데이터 주소를 참조하지 않게 한다.
    grid = [r[:] for r in data]
    # 처음에 찾은 바이러스 위치를 그대로 사용한다.
    queue = deque(temp)
    c = 0
    while queue:
        x, y = queue.popleft()
        # 기존에 갱신한 안전지대 개수보다 작아지면 탐색 중단
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


# 연구소에서 벽을 설치할 수 있는 경우를 모두 확인
def case(r=0, c=0, depth=0):
    global result
    if depth == 3:  # 벽 3개 설치 후 바이러스 이동을 확인
        c = bfs()
        if c != -1: # 백트래킹 시 그대로 종료, 아닐 경우 최대 안전지대를 갱신
            result = max(result, zero - c)
        return
    # 이전 case에서 같은 행, 같은 열부터 다시 탐색할 수 있도록
    for i in range(r, N):
        for j in range(M):
            if r == i and c > j: continue
            if data[i][j] == 0:
                data[i][j] = 1
                case(i, j, depth + 1)
                data[i][j] = 0


N, M = map(int, input().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
temp = []   # 바이러스 위치 저장용
for di in range(N):
    for dj in range(M):
        if data[di][dj] == 2:
            temp.append([di, dj])
zero = -3   # 벽은 꼭 3개가 설치되야 하므로 빈 공간의 개수 -3을 한다.
result = 0
for q in range(N):  # 빈 공간의 수를 확인
    zero += data[q].count(0)
case()
print(result)
