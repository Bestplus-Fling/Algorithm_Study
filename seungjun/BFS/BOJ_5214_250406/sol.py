import sys
sys.stdin = open('input.txt', 'r')
######################################
import sys
input = sys.stdin.readline
from collections import deque, defaultdict

n, k, m = map(int, input().split())
# 하이퍼튜브 정보를 따로 저장, 하이퍼 튜브는 n + 1 + i번에 저장
hipertube = defaultdict(list)

for i in range(m):
    stations = list(map(int, input().split()))
    # 1 base, n + 1
    hipertube_node = n + 1 + i
    for station in stations:
        # 1:[10], 2,[10], 3[10] / 10:[1, 2, 3]
        hipertube[station].append(hipertube_node)
        hipertube[hipertube_node].append(station)

queue = deque()
# 1base의 역 개수 + m개의 hipertube
visited = [-1] * (n + 1 + m)
# 1번 역에서 N번 역까지 가는데 필요한 최소 역 수
# 1포함
visited[1] = 1
queue.append(1)

while queue:
    now = queue.popleft()
    if now == n:
        break

    for adj_stat in hipertube[now]:
        # -1이 아니면 방문 한 적이 있으므로 continue
        if visited[adj_stat] != -1: continue

        if n < adj_stat:
            # 하이퍼튜브라면 거리를 늘리지 않음
            visited[adj_stat] = visited[now]
        else:
            # 역이라면 거리 + 1
            visited[adj_stat] = visited[now] + 1
        queue.append(adj_stat)

# 방문한적 없으면 -1, 방문한적 있다면 거리 출력
print(visited[n])