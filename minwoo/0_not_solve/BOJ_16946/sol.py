# https://www.acmicpc.net/problem/16946
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
dxy = (1, 0), (0, 1), (-1, 0), (0, -1)


def bfs(sx, sy):
    global grid, ans, N, M, visited
    vit = set()
    vit.add((sx, sy))
    queue = [(sx, sy)]
    zero = []
    # 인접한 0들의 개수를 visited에 저장
    cnt = 0
    while queue:
        temp = []
        for x, y in queue:
            cnt += 1
            zero.append((x, y))
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if grid[nx][ny] == 1 or (nx, ny) in vit:
                    continue
                temp.append((nx, ny))
                vit.add((nx, ny))
        queue = temp
    for x, y in zero:
        visited[x][y] = cnt


N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visited[i][j] > 0:
            continue
        if grid[i][j] == 0:
            bfs(i, j)
print(*visited, sep='\n')
for i in range(N):
    ans = []
    for j in range(M):
        if grid[i][j] == 1:
            case = 1
            for di, dj in dxy:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                case += visited[ni][nj]
            ans.append(str(case))
        else:
            ans.append('0')
    print(''.join(ans))


