import sys
sys.stdin = open('input.txt', 'r')

R, C = map(int, sys.stdin.readline().split())
visited_row, visited_col = set(), set()
row, col = 0, C-1
rc, cc = 0, 0

i = 0
prev_row, prev_col = row, col
while True:
    i += 1
    # 짝수는 열을 변경
    if i % 2 == 0:
        col = C-1 - (col - cc)
        cc = -(1 if cc == 0 else 0)

    # 홀수는 행을 변경
    else:
        row = R-1 - (row + rc)
        rc = -(1 if rc == 0 else 0)
    if prev_row == row and prev_col == col:
        break
    prev_row, prev_col = row, col
print(f'{i-1}\n{row+1} {col+1}')
