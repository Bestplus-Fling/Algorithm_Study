import sys
sys.stdin = open("input.txt", "r")

'''
입력의 첫 줄에 두 정수 R과 C(2 ≤ R, C ≤ 50)가 주어진다. R은 행의 개수, C는 열의 개수이다.

두 번째 줄에는 R개의 줄에 각각 C개의 문자가 주어진다. 이 문자는 '#', 'X', '.'로만 이뤄져 있다. 'X'는 항상 영대문자이다.

출력
출력은 다섯 줄이다. 첫째 줄에는 해빈이가 아무 차도 부수지 않으면서 주차할 수 있는 공간의 개수, 둘째 줄은 차 한 대를 부수고 주차할 수 있는 공간의 개수, 셋째 줄은 차 두 대, 넷째 줄은 차 세 대, 다섯째 줄은 차 네 대를 부수고 주차할 수 있는 공간의 개수이다.
'''

import sys

sys.stdin = open("input.txt", "r")

R, C = map(int, input().split())
parking_area = [list(input().strip()) for _ in range(R)]


result = [0] * 5  # 0~4 대를 주차할때의 경우의 수 저장

for i in range(R - 1):
    for j in range(C - 1):
        block = [
            parking_area[i][j],
            parking_area[i][j + 1],
            parking_area[i + 1][j],
            parking_area[i + 1][j + 1]
        ]

        if '#' in block:
            continue  # 2*2 배열로 리스트 짜두고 그 안에 건물 있으면 컨티뉴


        cnt = 0
        for k in range(len(block)):
            if block[k] == 'X':
                cnt += 1

        result[cnt] += 1


for r in result:
    print(r)






