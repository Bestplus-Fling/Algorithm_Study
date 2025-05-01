import sys
sys.stdin = open('input.txt', 'r')
######################################
from collections import deque
input = sys.stdin.readline

n = int(input())
# 그래프 선언, 1 base 사용
graph = [[] for _ in range(n + 1)]
# 그래프 간선 정보 저장
while True:
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        break
    graph[x].append(y)
    graph[y].append(x)

# bfs 탐색, 회원 점수 검사
min_cnt = n
queue = deque()
candidates = []
# 각 정점에서 모든 노드를 방문하기 위한 회수
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    cnt = 0
    visited[i] = True
    queue.append((i, cnt))

    while queue:
        vertex, cnt = queue.popleft()

        for adj_v in graph[vertex]:
            if visited[adj_v]: continue
            visited[adj_v] = True
            queue.append((adj_v, cnt + 1))

    if min_cnt > cnt:
        min_cnt = cnt
        candidates = [i]
    elif min_cnt == cnt:
        candidates.append(i)

print(min_cnt, len(candidates))
print(*candidates)