import sys
sys.stdin = open('input1.txt', 'r')

from collections import deque


# 지역구가 정상적으로 나누어졌는지 확인하는 함수
def check(case):
    # 아직 0으로 처리된 구역 한 곳을 정점으로 하여 순회를 할 것이다.
    queue = deque()
    for j in range(1, N+1):
        if case[j] == 1: continue
        queue.append(j)
        case[j] = 2
        break

    # 만약 0으로 처리된 정점들이 이어졌다면 지역구는 2개만 나올 것이다.
    while queue:
        vtx = queue.popleft()
        for adj in graph[vtx]:
            if case[adj]: continue
            case[adj] = 2
            queue.append(adj)
    print('순회 완료', case[1::])
    set_case = set(case[1::])
    if 0 not in set_case and len(set_case) == 2:
        return True

    return False


# 순회용 함수(일단 모든 정점을 방문)
def f(svtx, area, cities):
    global result, sum_sims, sims
    queue = deque([svtx])
    # 구역들이 모두 선택되는 경우는 없다.
    while queue:
        vtx = queue.popleft()
        area[vtx] = 1
        if len(set(area[1::])) < 2:
            area[vtx] = 0
            continue
        # 지역구가 정상적으로 나뉘었는지 검증
        if check(area[::]):
            div = abs(sum_sims - (cities * 2))
            print(div)
            if div >= 0:
                result = min(div, result)
        for adj in graph[vtx]:
            if area[adj]: continue
            area[adj] = 1
            queue.append(adj)


N = int(input())
sims = [0]
graph = [[] for _ in range(N+1)]
sims.extend(list(map(int, input().split())))
sum_sims = sum(sims[1::])
for i in range(N):
    n, *arr = map(int, input().split())
    graph[i+1] = arr

# 1. 구역을 두 개의 선거구로 나눈다
    # 각 구역은 두 선거구 중 하나에 포함되어야 한다
# 2. 선거구는 구역을 적어도 하나 포함해야 한다
# 3. 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다.
result = float('inf')
temp = [0] * (N+1)
for i in range(1, N+1):
    print(f'{i}에서 시작')
    f(i, temp[::], sims[i])

print(result if result != float('inf') else -1)
