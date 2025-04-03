import sys
sys.stdin = open('input.txt','r')
#########################################
import sys
from collections import deque
input = sys.stdin.readline


def melt(i, j, arr):
    global dxy
    cnt = 0
    for dy, dx in dxy:
        ni, nj = i + dy, j + dx
        if ni < 0 or nj < 0 or n <= ni or m <= nj: continue
        if arr[ni][nj]: continue
        cnt += 1
    return cnt


def check_iceberg_area(arr):
    global n, m, dxy
    visited = [[False] * m for _ in range(n)]
    iceberg_group = 0

    for i, j in iceberg:
        if visited[i][j]:
            continue
        if not arr[i][j]:
            continue
        iceberg_group += 1
        # 빙산이 두 그룹 이상되면 break
        if iceberg_group > 1:
            return iceberg_group
        visited[i][j] = True
        queue.append((i, j))

        # 빙산 구역 bfs 탐색
        while queue:
            idx, jdx = queue.popleft()

            for dy, dx in dxy:
                ni, nj = idx + dy, jdx + dx
                if ni < 0 or nj < 0 or n <= ni or m <= nj:
                    continue
                if visited[ni][nj]:
                    continue
                if not arr[ni][nj]:
                    continue
                visited[ni][nj] = True
                queue.append((ni, nj))
    return iceberg_group


# 세로 n, 가로 m
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

queue = deque()
cnt = 1
iceberg = set()
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if arr[i][j]:
            iceberg.add((i, j))
while True:
    melt_candidate = [[0] * m for _ in range(n)]

    for i, j in iceberg:
        # 0개수만큼 빙산 녹이기
        melt_candidate[i][j] = melt(i, j, arr)

    remove_candidate = []
    for i, j in iceberg:
        if melt_candidate[i][j] > arr[i][j]:
            remove_candidate.append((i, j))
            arr[i][j] = 0
        else:
            arr[i][j] -= melt_candidate[i][j]

    for i, j in remove_candidate:
        iceberg.remove((i, j))

    iceberg_area = check_iceberg_area(arr)
    # print(iceberg_area)
    if iceberg_area == 2:
        break
    elif iceberg_area == 0:
        cnt = 0
        break
    else:
        cnt += 1

print(cnt)