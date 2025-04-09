import sys
sys.stdin = open("input1.txt", "r")
"""
1. 일부 칸에 폭탄을 설치해 놓는다, 모든 폭탄이 설치된 시간은 같다(0초)
2. 다음 1초 동안 봄버맨은 아무것도 하지 않는다.(1초)(입력값 출력)
3. 다음 1초 동안 폭탄이 설치외어 있지 않은 모든 칸에 폭탄을 설치한다.
-> 풀배열 (2초 후)
4. 1초가 지난 후에 3초 전 설치된 폭탄이 모두 폭발한다(3초 후)
5. 3과 4를 반복한다.
"""

dkx = (1, 0, -1, 0)
dky = (0, 1, 0, -1)


def bomb(check_grid):
    bomb_grid = set_bomb()
    for x in range(R):
        for y in range(C):
            if check_grid[x][y] == 'O':
                bomb_grid[x][y] = '.'
                for dx, dy in zip(dkx, dky):
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < R and 0 <= ny < C):
                        continue
                    bomb_grid[nx][ny] = '.'
    return bomb_grid


def set_bomb():
    temp = [['O'] * C for _ in range(R)]
    return temp


def printing(print_grid):
    for li in print_grid:
        print(''.join(li))


R, C, N = map(int, input().split())
default_grid = [list(input().strip()) for _ in range(R)]
full_grid = set_bomb()
if N == 1:
    printing(default_grid)
elif N % 2 == 0:
    printing(full_grid)
else:
    grid1 = bomb(default_grid)
    # print(*grid1, sep='\n', end='\n\n')
    mod = N % 4
    if mod == 3:
        # 처음 설치된 폭탄과 연계된 폭탄을 터뜨린다.
        printing(grid1)
    elif mod == 1:
        # 2번째에 설치한 폭탄과 연계된 폭탄을 터뜨린다.
        nd_grid = set_bomb()
        for i in range(R):
            for j in range(C):
                if grid1[i][j] == 'O':
                    nd_grid[i][j] = 'O'
                else:
                    nd_grid[i][j] = '.'
        printing(bomb(nd_grid))



