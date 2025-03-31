import sys
sys.stdin = open("input_1226.txt", "r")

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def find_three(start_x, start_y):
    if maze[start_x][start_y] == 3:
        return 1

    for dx, dy in dxy:
        nx = start_x + dx
        ny = start_y + dy

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != 1 and maze[nx][ny] != 1: # 방문 ,벽, 체크
            visited[nx][ny] = 1

            if find_three(nx,ny):
                return 1

    return 0

T = 10
for tc in range(1, T+1):
    test_case = int(input())
    n = 16
    maze = [list(map(int, input().strip())) for _ in range(n)] # 16 x 16 배열을 받는다
    visited = [[0] * n for _ in range(n)] # visited배열에 +1을 해줘야 하나 생각했지만 그건 트리 구조에서만 0번을 버려서 +1

    # 2가 시작점이니까 2를 찾음
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                result = find_three(i,j)



    print(f"#{test_case}", result)
