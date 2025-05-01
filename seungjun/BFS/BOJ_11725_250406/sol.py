import sys
sys.stdin = open('input.txt', 'r')
######################################
import sys
input = sys.stdin.readline

n = int(input())
# 1 base, 양방향 그래프로 구성해두기
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 1번을 Root로 그래프 탐색
visited = [False] * (n + 1)
parent = list(range(n + 1))
stack = [1]

while stack:
    node = stack.pop()
    visited[node] = True
    # 자식 순회
    for adj in graph[node]:
        if visited[adj]: continue
        # 부모 기록
        parent[adj] = node
        stack.append(adj)

print(*parent[2:], sep='\n')