import sys
sys.stdin = open('input.txt', 'r')
dkx = [1, 0, -1, 0]
dky = [0, 1, 0, -1]


def delta(x, y):
    global case_bomb
    for dx, dy in zip(dkx, dky):
        nx, ny = x + dx, y + dy
        if not(0 <= nx < R and 0 <= ny < C):
            continue
        case_bomb[nx][ny] = '.'
    case_bomb[x][y] = '.'


def printing(arr):
    for a in arr:
        print(''.join(a))


R, C, N = map(int, input().split())
default = [list(input().strip()) for _ in range(R)]
set_bomb = [['O'] * C for _ in range(R)]
mod = N % 10

if mod in [1, 5, 9]:
    printing(default)
elif mod in [3, 7]:
    case_bomb = [r[::] for r in set_bomb]
    for i in range(R):
        for j in range(C):
            if default[i][j] == 'O':
                delta(i, j)
    printing(case_bomb)
else:
    printing(set_bomb)

# # print(*default, sep='\n', end='\n\n')
# # print(*set_bomb, sep='\n', end='\n\n')
# case_bomb = [r[::] for r in set_bomb]
# for i in range(R):
#     for j in range(C):
#         if default[i][j] == 'O':
#             delta(i, j)
# # print(*case_bomb, sep='\n')
#
# if N % 3 == 0 and N > 0:
#     printing(case_bomb)
# elif N % 2 == 0:
#     printing(set_bomb)
# else:
#     printing(default)
