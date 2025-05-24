import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
"""
계한으로 계란을 치게 되면 어떤 일이 일어나는가
1. 각 계란에는 내구도와 무게가 정해져있다.
계란으로 계란을 치면 각 계란의 내구도는 상대 계란의 무게만큼 깎이게 된다
그리고 내구도가 0 이하가 되는 순간 계란은 깨지게 된다.
예) 계란1의 내구도 7, 무게 5
계란 2의 내구도 3, 무게 4 일때
계란 1로 계란 2를 치게 되면 계란 1의 내구도는 계란 2의 무게(4) 만큼 감소
계란 2의 내구도는 계란 1의 무게(5)만큼 감소해 -2가 된다
계란 1은 깨지 않고 계란 2는 개짐

일렬로 놓여있는 계란에 대해 왼쪽부터 차례로 들어서 한번씩만 다른 계란을 쳐 최대한 많은 
계란을 깨는 문제
1. 가장 왼쪽의 계란을 든다.
2. 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다
단 손에 든 계란이 깨졌거나 / 깨지지 않은 다른 계란(?)이 없으면 치지 않고 넘어간다.
이후 손에 든 계란을 원래 자리에 내려놓고 3번 과정을 진행
3. 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행
단, 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란을 치는 과정을 종료

이 과정을 통해 최대한 많은 계란을 깨는 것
"""


def dfs(depth):
    global N, ans, eggs
    if depth == N:
        # 계란 전체를 확인
        count = 0
        for e in range(N):
            if eggs[e][0] <= 0:
                count += 1
        ans = max(ans, count)
        return
    # 1. 1번 계란을 드는 건 수순
    # 2. 그 계란으로 자기 자신의 계란을 제외한 다른 계란을 친다.
    # 3. 내 계란을 내려놓고 그 다음 계란을 손에 쥔다.
    # depth는 현재 내가 들고 있는 계란을 의미한다.
    # depth의 계란이 깨졌다면 다음 계란을 잡으러 간다
    if eggs[depth][0] <= 0:
        dfs(depth+1)
    else:
        for i in range(N):
            if depth == i: continue
            # depth 달걀로 i 달걀을 쳤을때
            if eggs[i][0] <= 0:
                dfs(depth + 1)
            else:
                # 만약 쳤는데 깨지지 않았다면 그냥 넘어간다.
                eggs[depth][0] -= eggs[i][1]
                eggs[i][0] -= eggs[depth][1]

                dfs(depth+1)

                eggs[depth][0] += eggs[i][1]
                eggs[i][0] += eggs[depth][1]


N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0)
print(ans)