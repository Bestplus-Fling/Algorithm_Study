import sys
sys.stdin = open('input.txt', 'r')

"""
매 1분마다 이벤트 맵은 A만큼, 심신 수련관은 B만큼, VIP 사우나는 C만큼 경험치를 올려준다
심신 수련관과 VIP 사우나에 입장하기 위해서는 별도의 입장권이 필요하고,
입장하면 30분동안 있을 수 있다.
레벨을 1 올리려면 경험치가 100 만큼 필요하다
100을 초과한 경험치즌 레벨 업때 사라지지 않고 이월된다

이벤트 맵, 심신 수련관, 사우나의 분당 얻을 수 있는 경험치와
수련관과 사우나의 입장권 개수
육성 캐릭터의 현재 레벨이 주어질 때
임스가 잠수맵만 통하여 250레벨을 몇 분 뒤에 달성할 수 있는 지 구하시오
"""


def f(up):
    global exp, time
    for i in range(30):
        exp -= up
        time += 1
        if exp <= 0:
            return True
    return False


A, B, C = map(int, input().split())
S, V = map(int, input().split())
now_level = int(input())
# 필요한 경험치를 계산

exp = (250 - now_level) * 100
# print(exp)
# 입장 가능한 곳부터 간다
# 계산식 (1분당 B, C만큼 증가 * 30분) * 입장권 개수
# 일단 while문으로
count = 30
time = 0
while True:
    if V > 0:
        # 함수를 부른다.
        # 함수 안에서 True가 발생하면 그 즉시 while문을 종료
        V -= 1
        if f(C):
            break
    elif S > 0:
        S -= 1
        if f(B):
            break
    else:
        if f(A):
            break
print(time)
