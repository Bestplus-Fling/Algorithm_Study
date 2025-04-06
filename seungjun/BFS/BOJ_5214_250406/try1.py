import sys
sys.stdin = open('input.txt', 'r')

from collections import deque, defaultdict

n, k, m = map(int, input().split())
graph = defaultdict(list)

# 역: 1~n / 하이퍼튜브: n+1 ~ n+m
for i in range(m):
    stations = list(map(int, input().split()))
    hyper_node = n + i + 1  # 하이퍼튜브 노드 번호
    for station in stations:
        graph[station].append(hyper_node)
        graph[hyper_node].append(station)

print(graph)
# BFS 탐색
visited = [False] * (n + m + 2)
q = deque()
q.append((1, 1))  # (현재 역, 거리)
visited[1] = True

while q:
    curr, dist = q.popleft()
    print('탐색', curr)
    if curr == n:
        print('목표', dist)
        break
    for next_node in graph[curr]:
        if not visited[next_node]:
            print('미 방문 탐색', curr, next_node)
            visited[next_node] = True
            # 하이퍼튜브일 경우: 역으로 가는 거리는 증가하지 않음
            # 역일 경우: 실제 거리 1 증가
            if next_node > n:
                print('하이퍼링크', curr, 'to', next_node)
                q.append((next_node, dist))
            else:
                print('실제 역', curr, 'to', next_node)
                q.append((next_node, dist + 1))
    print(visited)
else:
    print(-1)
