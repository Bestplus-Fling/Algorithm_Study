import sys
sys.stdin = open('input.txt','r')
#########################################
#쌀 개수, 반지름
N, R = map(int, input().split())
rice = [tuple(map(int, input().split())) for _ in range(N)]

max_count = 0
answer = (0, 0)

# 웍의중심 후보를 최대한 많이 해봄
for cx in range(-100, 101):
    for cy in range(-100, 101):
        count = 0
        #쌀의 좌표
        for x, y in rice:
            # 문제에 나와있듯이 (x웍의 좌표- x쌀의 좌표)제곱+(y웍의 좌표- y쌀의 좌표)제곱 <=R제곱
            #이 범위 안에들어가면 쌀이 들어갔다는것
            if (cx - x) ** 2 + (cy - y) ** 2 <= R ** 2:
                count += 1
                #만약 카운트가 맥스 카운트보다 크면 그게 맥스 카운트임 그리고 앤서에 웍위 위치 넣기
        if count > max_count:
            max_count = count
            answer = (cx, cy)

print(answer[0], answer[1])

