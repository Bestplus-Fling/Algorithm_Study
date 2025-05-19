import sys
sys.stdin = open('input.txt', 'r')
INF = float('inf')
# 현재 가지고 있는 돈을 넘어서는 경로는 이동할 수 없다
# 현재 경로에서 도착 정점까지 이동하는 데 최대 수금액도 함께 제시해야 한다
# 이때 지나갈 수 있는 경로에서 최대 가중치가 가장 낮은 경우에 최대값을 반환해야 한다.


def dfs(distance, q, away):
    global result
    dist, vtx = q.pop()
    if dist > C:
        return
    if dist > distance[vtx]:
        return
    if vtx == B:
        # 도착지까지 오면서의 각 경로마다 가중치 중 최대
        max_py = max(away)
        result = min(result, max_py)
        return
    for adj, w in graph[vtx]:
        if (acc := w + dist) >= distance[adj]:
            continue
        distance[adj], d = acc, distance[adj]
        q.append((acc, adj))
        dfs(distance, q, away+[w])
        if q:
            q.pop()
        distance[adj] = d
    pass


N, M, A, B, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    v, a, p = map(int, input().split())
    graph[v].append((a, p))
    graph[a].append((v, p))
result = INF
temp = [INF]*(N+1)
temp[A] = 0
dfs(temp, [(0, A)], [])
print(result if result != INF else -1)