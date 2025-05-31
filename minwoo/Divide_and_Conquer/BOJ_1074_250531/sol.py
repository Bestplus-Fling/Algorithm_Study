import sys
sys.stdin = open('input.txt', 'r')


def dfs(n, r, c):
    global num, ans
    # n > 1일 경우 배열을 크기가 2 ** n-1 로 4등분한 후에 재귀적으로 방문
    if n > 1:
        k = 2 ** (n-1)
        # print(f'N={n}일 때 {k} 길이 만큼 분할')
        for i in range(r, r+(k*2), k):
            check_row = set(range(i, i + k))
            for j in range(c, c+(k*2), k):
                # 여기서 목표하는 row, col에 진입하는 dfs인지 검증
                if row not in check_row and col not in set(range(j, j+k)):
                    num += k * k
                    continue
                # print(i, j)
                dfs(n-1, i, j)
        return
    for i in range(r, r+2):
        for j in range(c, c+2):
            if (i, j) == (row, col):
                ans = num
            num += 1


N, row, col = map(int, input().split())
width = 2 ** N
num = 0
ans = -1
# print(width)
dfs(N, 0, 0)
# print(*grid, sep='\n')
print(ans)