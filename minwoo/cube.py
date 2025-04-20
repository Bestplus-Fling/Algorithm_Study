import sys
sys.stdin = open('input.txt', 'r')
"""
동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4

grid[x][y] == 0 => 주사위의 바닥면에 쓰여 있는 수가 칸에 복사

grid[x][y] != 0 => 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사, 
칸에 쓰여 있는 수는 0이 된다

주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며
"""



N, M, xx, yy, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
commend = list(map(int, input().split()))
print(grid)
print(commend)