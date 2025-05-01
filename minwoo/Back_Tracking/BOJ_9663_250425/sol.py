import sys
sys.stdin = open('input.txt', 'r')


def is_valid(row, col):
    global col_visited, diagonal_visited
    # 위쪽, 대각선 위 확인
    if col_visited[col]:
        return False
    for x, y in diagonal_visited:
        if abs(row - x) == abs(col - y):
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
            diagonal_visited.append((row, col))
            n_queen(row+1)
            col_visited[col] = 0
            diagonal_visited.pop()


N = int(input())
col_visited = [0] * N
diagonal_visited = []
ans = 0
n_queen(0)
print(ans)
