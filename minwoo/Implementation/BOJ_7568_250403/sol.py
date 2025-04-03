import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
player = []
rank = [1] * N
for i in range(N):
    h, w = map(int, input().split())
    player.append((i, h, w))
player.sort(key=lambda x: (-x[1], -x[2]))

cnt, k = 1, 1
visited = [False] * N
for i in range(N):
    v, x, y = player[i]
    if visited[v]: continue
    for j in range(N):
        o, p, q = player[j]
        if x < p and y < q:
            rank[v] += 1
            visited[v] = True
        elif (x > p and y < q) or (x < p and y > q):
            if visited[o]: continue
            rank[o] = rank[v]
            visited[v], visited[o] = True, True
            break
    # print(f'현재 선수 {v}, {rank}')
print(*rank)
