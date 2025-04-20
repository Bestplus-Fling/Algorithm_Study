import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def bfs():
    global graph, N, M
    queue = []
    count = ['-1'] * (N+1)
    visited = set()

    for adj, w in graph[1]:
        queue.append((adj, w))
        visited.add((adj, w))
    cnt = 1
    while queue:
        temp = []
        for vtx, weight in queue:
            if count[vtx] == '-1':
                count[vtx] = str(cnt)
            for adj, w in graph[vtx]:
                if (adj, w) in visited: continue
                if abs(weight - w) == 1:
                    temp.append((adj, w))
                    visited.add((adj, w))
        queue = temp
        cnt += 1
    return [count[i] for i in range(1, N+1)]


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
print(' '.join(bfs()))
