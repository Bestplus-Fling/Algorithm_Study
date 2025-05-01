import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def is_valid(nrow, ncol):
    # 모든 좌표의 끝과 끝은 연결되어 있다.
    # 만약 -1, -1일 경우 3, 3으로 이동한다.
    if nrow >= N:
        nrow %= N
    elif nrow < 0:
        nrow = (N + nrow) % N

    if ncol >= N:
        ncol %= N
    elif ncol < 0:
        ncol = (N + ncol) % N
    return nrow, ncol


def assembly(data_list, x, y):
    cnt = len(data_list)
    # print(cnt)
    # r, c, m, s, d
    odd, even = 0, 0
    sum_mass, sum_speed = 0, 0
    for temp in data_list:
        sum_mass += temp[2]
        sum_speed += temp[3]
        if temp[4] % 2 == 0:
            even += 1
        else:
            odd += 1
    # 각 파이어볼의 질량 = sum(fireball.m) / 5
    div_mass = sum_mass // 5
    # 각 파이어볼의 속력 = sum(fireball.s) / count(fireball)
    div_speed = sum_speed // cnt
    # print(f'속력 : {div_speed}, mess : {div_mass}')
    # 질량이 0인 파이볼은 소멸되어 없어진다.
    if div_mass == 0:
        return
    if odd == cnt or even == cnt:
        # 합쳐지는 파이어볼의 방향이 모두 홀수이거나, 모두 짝수인 경우
        # 방향은 0, 2, 4, 6
        for dir in range(0, 7, 2):
            data.append([x, y, div_mass, div_speed, dir])
    else:   # 그렇지 않을 경우 방향은 1, 3, 5, 7
        for dir in range(1, 8, 2):
            data.append([x, y, div_mass, div_speed, dir])


def search():
    global grid
    for x in range(N):
        for y in range(N):
            length = len(grid[x][y])
            # print(f'now ({x}, {y}), data count : {length}')
            if length == 0: continue
            elif length >= 2:
                assembly(grid[x][y], x, y)
            else:
                data.append(grid[x][y][0])
            grid[x][y] = []


N, M, K = map(int, sys.stdin.readline().split())
# r: 행, c: 열, m: 질량, s: 속력, d: 방향(문제 참조)
data = deque()
for i in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    r, c = r - 1, c - 1
    data.append([r, c, m, s, d])

grid = [[[] for q in range(N)] for _ in range(N)]


"""
1. 모든 파이어볼이 자신의 방향 d로 속력 s칸 만큼 이동
    - 이동한 중에 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음에 따라서 처리
    1. 같은 칸에 있는 파이볼은 모두 하나로 합쳐진다.
    2. 파이어볼은 4개의 파이어볼로 나누어진다.
        1. 각 파이어볼의 질량 = sum(fireball.m) / 5
        2. 각 파이어볼의 속력 = sum(fireball.s) / count(fireball)
        3. 합쳐지는 파이어볼의 모두 홀수, 혹은 짝수인 경우, 방향은 0, 2, 4, 6 
           그렇지 않을 경우 1, 3, 5, 7 방향이 된다
    4. 질량이 0인 파이어볼은 소멸되어 없어진다.
"""

# 파이어볼의 이동 구현
for k in range(K):  # K번 명령이 이루어진다.
    while data:
        # 파이어볼의 이동,
        r, c, m, s, d = data.popleft()
        # print(f'속력{s}, 방향{d}')
        # print(f'변경전 좌표 = {r}, {c} / 변경된 좌표 = {nr}, {nc}')
        nr, nc = is_valid(r + (dx[d] * s), c + (dy[d] * s))
        # print(f'검증된 좌표 : {nr}, {nc}')
        grid[nr][nc].append([nr, nc, m, s, d])
    print(*grid, sep='\n')
    print()
    # break
    # 결합된 경우를 탐색
    # print(data)
    search()

remain_mass = 0
for fire in data:
    remain_mass += fire[2]
print(remain_mass)
