import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
dxy = (1, 0), (0, 1), (-1, 0), (0, -1)


def dfs():
    global data, result, dxy
    stack = set()
    stack.add((0, 0, 1, data[0][0]))
    while stack:
        x, y, cnt, visit = stack.pop()
        result = max(result, cnt)
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if (k := data[nx][ny]) in visit:
                continue
            stack.add((nx, ny, cnt+1, visit+k))


R, C = map(int, input().split())
data = [list(input().strip()) for _ in range(R)]
result = 0
dfs()
print(result)
