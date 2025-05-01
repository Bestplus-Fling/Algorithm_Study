import sys
sys.stdin = open('input.txt', 'r')
#########################################


'''
F 는 앞으로 한칸 이동 

L과 R은 방향을 왼쪽 또는 오른쪽으로 전환
90도 회전은 하지만 위치는 그대로


x랑 y를 찾아서 #으로 된 배열 만들고
가는 곳 마다 .으로 바꾸면 될듯
'''

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


n = int(input())
naeyong = list(input())

x = y = 0
xy = [[x, y]]
h = 0
for i in range(n):
    if naeyong[i] == 'R':
        h = (h + 1) % 4
    elif naeyong[i] == 'L':
        h = (h - 1) if h > 0 else 3
    elif naeyong[i] == 'F':
        x, y = x + dx[h], y + dy[h]
        xy.append([x, y])


sx = sorted(xy, key=lambda k: k[0])
sy = sorted(xy, key=lambda k: k[1])

minx = sx[0][0]
miny = sy[0][1]

if minx < 0:
    minx1 = abs(minx)
    for i in range(len(sx)):
        sx[i][0] += minx1

if miny < 0:
    miny1 = abs(miny)
    for i in range(len(sy)):
        sy[i][1] += miny1

q, p = sx[-1][0] + 1, sy[-1][1] + 1

arr = [['#'] * p for _ in range(q)]

for z, c in xy:
    arr[z][c] = '.'

for i in arr:
    print(''.join(i))



