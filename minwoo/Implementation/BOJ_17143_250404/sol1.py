import sys
sys.stdin = open('input1.txt', 'r')
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


# 해야 할 일
"""
1. 상어의 속도를 이용해서 이동할 좌표를 한번에 계산하는 로직
2. catched를 사용해 이미 잡힌 상어는 스택 접근을 제한
3. stack의 데이터를 삭제, 삽입하는게 아니라 
갱신할 수 있도록 한다. -> 2차원 배열 없어도 됨
4. 
"""
def move():
    global stack, data
    temp = []
    for row, col in stack:
        if data[row][col] == '.': continue
        x, y = row, col
        s, d, size = data[row][col]
        data[row][col] = '.'
        for q in range(s):
            if not(0 <= x + dx[d] < R and 0 <= y + dy[d] < C):
                if d < 2:
                    d = 0 if d else 1
                else:
                    d = 2 if d == 3 else 3
            x, y = x + dx[d], y + dy[d]
        temp.append([x, y, s, d, size])
    stack = []
    for x, y, s, d, size in temp:
        # 이미 있는 상어의 크기가 더 크다면 갱신 X
        if data[x][y] != '.' and data[x][y][2] > size:
            continue
        # 상어가 없다면 그냥 저장
        data[x][y] = (s, d, size)
        stack.append((x, y))


R, C, M = map(int, sys.stdin.readline().split())
data = [['.'] * C for _ in range(R)]
stack = []
for i in range(M):
    r, c, speed, direction, z = map(int, sys.stdin.readline().split())
    # 저장 순서(속력, 이동 방향, 크기)
    data[r-1][c-1] = (speed, direction-1, z)
    stack.append((r-1, c-1))
# 이동 방향 1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽
Kg = 0
for j in range(C):  # 1. 낚시왕이 물고기를 잡는다
    for i in range(R):
        if data[i][j] == '.': continue
        Kg += data[i][j][2]
        data[i][j] = '.'
        break
    # 상어를 잡고, 낚시왕이 이동하기 전에 상어가 이동한다
    move()
print(*data, sep='\n')
print(Kg)
