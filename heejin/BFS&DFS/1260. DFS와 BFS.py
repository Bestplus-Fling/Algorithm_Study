import sys
from collections import deque

sys.stdin = open("1260. DFS와 BFS.txt")


def dfs(v):

    visited[v] = True
    result_dfs.append(v)

    for adj in graph[v]:
        if not visited[adj]:
            dfs(adj)


def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True

    while queue:
        node = queue.popleft()
        result_bfs.append(node)

        for adj in graph[node]:
            if not visited_bfs[adj]:
                visited_bfs[adj] = True
                queue.append(adj)


n, m, v = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
visited = [False] * (n + 1)
visited_bfs = [False] * (n + 1)
result_dfs=[]
result_bfs=[]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for key in graph.keys():
    graph[key].sort()


dfs(v)
bfs(v)

print(*result_dfs)
print(*result_bfs)
