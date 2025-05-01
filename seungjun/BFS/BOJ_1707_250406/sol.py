import sys
sys.stdin = open('input.txt', 'r')
######################################
import sys
input = sys.stdin.readline
from collections import deque


def bfs(graph):
    queue = deque()
    visited = [0] * (v + 1)

    # 모든 정점이 연결되지 않은 경우도 생각해야 함!
    for node in range(1, v + 1):
        if visited[node]: continue
        visited[node] = node
        queue.append(node)

        while queue:
            vertex = queue.popleft()

            for adj_v in graph[vertex]:
                # 사이클이 있다면 visited 검사
                if visited[adj_v]:
                    if (visited[adj_v] + visited[vertex]) % 2 == 0:
                        return 'NO'
                    else:
                        continue
                visited[adj_v] = visited[vertex] + 1
                queue.append(adj_v)

    return 'YES'


T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    # 1 base
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    print(bfs(graph))
