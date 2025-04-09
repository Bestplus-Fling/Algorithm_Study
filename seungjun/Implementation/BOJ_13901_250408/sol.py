import sys
sys.stdin = open('input.txt','r')
#########################################
import sys
input = sys.stdin.readline

# 로봇의 이동방향
move = {
    1: (-1, 0),
    2: (1, 0),
    3: (0, -1),
    4: (0, 1)
}

# 입력
r, c = map(int, input().split())
visited = [[False] * c for _ in range(r)]
# 장애물 입력
k = int(input().strip())
for _ in range(k):
    x, y = map(int, input().split())
    visited[x][y] = True
# 로봇의 시작지점
robot = list()
i, j = map(int, input().split())
visited[i][j] = True
# 로봇의 이동방향 순서
move_sequence = list(map(int, input().split()))

sequence = 0
finish = 0
while True:
    if finish > 3:
        break
    sequence = sequence % 4
    dy, dx = move[move_sequence[sequence]]
    ni, nj = i + dy, j + dx
    if ni < 0 or nj < 0 or r <= ni or c <= nj:
        finish += 1
        sequence += 1
        continue
    if visited[ni][nj]:
        finish += 1
        sequence += 1
    else:
        finish = 0
        visited[ni][nj] = True
        i, j = ni, nj

print(i, j)