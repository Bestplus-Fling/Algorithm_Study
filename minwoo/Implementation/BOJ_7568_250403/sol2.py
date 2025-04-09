import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
player = []
for i in range(N):
    player.append((i, *list(map(int, input().split()))))
rank = [1] * N
player.sort(key=lambda x: (-x[1], -x[2]))
for i in range(N):
    w, x, y = player[i]
    for j in range(N):
        o, p, q = player[j]
        if x < p and y < q:
            rank[w] += 1
print(*rank)
