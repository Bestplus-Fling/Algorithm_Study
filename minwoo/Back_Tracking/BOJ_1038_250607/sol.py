import sys
sys.stdin = open("input.txt", "r")

"""
x의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면
그 수를 감소하는 수라고 한다

321과 950은 감소하는 수
322와 958은 아니다

0, 1, 2, 3, 4, 5, 6, 7, 8, 9
10
20 21
30 31 32
40 41 42 43
50 51 52 53 54
60 61 62 63 64 65
70 71 72 73 74 75 76
80 81 82 83 84 85 86 87
90 91 92 93 94 95 96 97 98
210
310 320 321
410 420 421 430 431 432
510 520 521 530 531 532 540 541 542 543

"""
# 총 9자리(987654321)까지
# dfs로 9번의 깊이로 만들어낼 수 있다
# _list = list(range(10))
_list = []


def dfs(depth, nums, prev):
    global _list, stop
    """
    1. 0부터 9은 리스트에 포함된 상태,
    2. 내 앞의 자리수랑 같아지기 전까지 for, 깊이 우선 탐색
    """
    if depth == stop:
        # print('조합용 수:', nums, depth)
        # print(temp := list(*combinations(nums, depth)))
        # print(temp := ''.join(map(str, nums)))
        # _list[idx] = int(''.join(map(str, nums)))
        _list.append(int(''.join(map(str, nums))))
        return
    if prev is None:
        prev = 10
    for i in range(0, prev):
        dfs(depth+1, nums+[i], i)


N = int(input())
# 감소하는 수의 개수를 알아야 한다
# 순열인가?
stop = 1
while stop != 11:
    dfs(0, [], None)
    stop += 1
try:
    print(_list[N])
except:
    print(-1)