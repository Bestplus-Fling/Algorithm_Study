import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def is_valid(row, col):
    global col_visited, diagonal_visited
    # 위쪽, 대각선 위 확인
    print('검증', row, col)
    if col_visited[col]:
        return False
    for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
        if (r, c) in diagonal_visited:
            return False
        if (case := col + (col - c)) < N:
            print(r, case)
            if (r, case) in diagonal_visited:
                return False
    return True


def n_queen(row):
    global ans, col_visited, diagonal_visited
    if row == N:
        ans += 1
        return
    for col in range(N):
        if is_valid(row, col):
            col_visited[col] = 1
            diagonal_visited.add((row, col))
            n_queen(row+1)
            col_visited[col] = 0
            diagonal_visited.remove((row, col))


N = int(input())
col_visited = [0] * N
diagonal_visited = set()
ans = 0
n_queen(0)
print(ans)
