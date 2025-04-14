import sys
sys.stdin = open('input2.txt', 'r')
from collections import deque


def BFS():
    global W, H, K, grid, result
    visited = [[[False] * W for _ in range(H)] for __ in range(K+1)]
    dkx = [1, 0, -1, 0]
    dky = [0, 1, 0, -1]
    knight_x = [-1, -2, -2, -1, 1, 2, 2, 1]
    knight_y = [-2, -1, 1, 2, 2, 1, -1, -2]
    queue = deque([(0, 0, K, 0)])
    visited[K][0][0] = True
    while queue:
        x, y, k, cnt = queue.popleft()
        if (x, y) == (H-1, W-1):
            result = cnt
            return
        cnt += 1
        if k > 0:
            for knx, kny in zip(knight_x, knight_y):
                nx, ny = x + knx, y + kny
                if not(0 <= nx < H and 0 <= ny < W): continue
                if visited[k-1][nx][ny]: continue
                if grid[nx][ny] == 1: continue
                queue.append((nx, ny, k-1, cnt))
                visited[k-1][nx][ny] = True
        for dx, dy in zip(dkx, dky):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < H and 0 <= ny < W): continue
            if visited[k][nx][ny]: continue
            if grid[nx][ny] == 1: continue
            queue.append((nx, ny, k, cnt))
            visited[k][nx][ny] = True


K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]
result = float('inf')
BFS()
print(result if result != float('inf') else -1)
