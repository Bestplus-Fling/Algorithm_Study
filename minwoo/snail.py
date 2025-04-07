import sys
sys.stdin = open('input.txt', 'r')

R, C = map(int, input().split())
visited_row, visited_col = set(), set()
row, col = 0, C-1
rc, cc = 0, 0
# stop_row, stop_col =
i = 0
while True:
    i += 1
    # 짝수는 열을 변경
    if i % 2 == 0:
        col = C-1 - (col - cc)
        if col in visited_col:
            break
        visited_col.add(col)
        cc = -(1 if cc == 0 else 0)

    # 홀수는 행을 변경
    else:
        row = R-1 - (row + rc)
        if row in visited_row:
            break
        visited_row.add(row)
        rc = -(1 if rc == 0 else 0)


print(f'{i-1}\n{row+1} {col+1}')
