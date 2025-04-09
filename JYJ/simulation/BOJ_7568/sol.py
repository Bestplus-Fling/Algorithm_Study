import sys

sys.stdin = open("input.txt", "r")

#########################################

'''
사회자가 몇 번째 수를 부른 후 철수가 빙고를 외치게 되는지 출력

'''

def check_bingo():
    count = 0
    for i in range(5):
        bingo_line = True
        for j in range(5):
            if bingo[i][j] == 0:
                bingo_line = False
                break
        if bingo_line:
            count += 1


    for i in range(5):
        bingo_line = True
        for j in range(5):
            if bingo[j][i] == 0:
                bingo_line = False
                break
        if bingo_line:
            count += 1


    bingo_line = True
    for i in range(5):
        if bingo[i][i] == 0:
            bingo_line = False
            break
    if bingo_line:
        count += 1


    bingo_line = True
    for i in range(5):
        if bingo[i][4 - i] == 0:
            bingo_line = False
            break
    if bingo_line:
        count += 1

    return count


chulsu = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]
bingo = [[0] * 5 for _ in range(5)]
result = 0

for i in range(5):
    for j in range(5):
        num = mc[i][j]
        result += 1
        for x in range(5):
            for y in range(5):
                if chulsu[x][y] == num:
                    bingo[x][y] = 1
        if check_bingo() >= 3:
            print(result)
            exit()