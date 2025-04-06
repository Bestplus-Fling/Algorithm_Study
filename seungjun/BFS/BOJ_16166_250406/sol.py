import sys
sys.stdin = open('input.txt', 'r')
######################################
import sys
input = sys.stdin.readline
from collections import deque, defaultdict

n = int(input())
stations = defaultdict(list)

for i in range(n):
    line, *station_info = map(int, input().split())
    # 1호선은 stations -1, 2호선은 stations -2
    subway = -(i + 1)
    for station in station_info:
        stations[station].append(subway)
        stations[subway].append(station)
# 도착 역 정보
target = int(input())

queue = deque()
visited = set()

# 출발역, 출발 호선 번호 추가
visited.add(0)
# 출발역이 도착역과 동일한 경우를 추가
queue.append((0, 0))
for line in stations[0]:
    visited.add(line)
    # 호선 번호, 환승 횟수
    queue.append((line, 0))
# 환승 회수를 저장할 변수
result = -1

while queue:
    now, cnt = queue.popleft()

    if now == target:
        result = cnt
        break

    for adj_v in stations[now]:
        if adj_v in visited:
            continue
        if adj_v < 0:
            # 다른 호선이라면 환승 추가
            visited.add(adj_v)
            queue.append((adj_v, cnt + 1))
        else:
            # 역 정보라면 환승 추가하지 않음
            visited.add(adj_v)
            queue.append((adj_v, cnt))

print(result)