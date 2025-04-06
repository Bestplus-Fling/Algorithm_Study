'''
빙고 게임은 다음과 같은 방식으로 이루어진다.

먼저 아래와 같이 25개의 칸으로 이루어진 빙고판에 1부터 25까지 자연수를 한 칸에 하나씩 쓴다
다음은 사회자가 부르는 수를 차례로 지워나간다. 예를 들어 5, 10, 7이 불렸다면 이 세 수를 지운 뒤 빙고판의 모습은 다음과 같다.
차례로 수를 지워가다가 같은 가로줄, 세로줄 또는 대각선 위에 있는 5개의 모든 수가 지워지는 경우 그 줄에 선을 긋는다.
이러한 선이 세 개 이상 그어지는 순간 "빙고"라고 외치는데, 가장 먼저 외치는 사람이 게임의 승자가 된다.
철수는 친구들과 빙고 게임을 하고 있다. 철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때, 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 출력하는 프로그램을 작성하시오.
입력
첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.
'''

import sys
sys.stdin = open('input.txt','r')
#########################################
board = [list(map(int, input().split())) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)] #방문체크

numbers = []
for _ in range(5):
    arr = list(map(int, input().split()))
    numbers += arr # 가로로 받기위해서 이렇게함


def find(num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num: #만약 보드 순회 값이 사회자가 부르는 숫자와 같으면
                visited[i][j] = True #방문체크
def bingo():
    count = 0 #카운트

    for i in range(5): #가로
        cnt_1 = 0
        for j in range(5):
            if visited[i][j] == True:
                cnt_1 += 1
                if cnt_1 == 5:
                    count += 1


    for i in range(5):#세로
        cnt_2 = 0
        for j in range(5):
            if visited[j][i] == True:
                cnt_2 += 1
                if cnt_2 == 5:
                    count += 1


    cnt_3 = 0
    for i in range(5):
        if visited[i][i] ==True: #대각
            cnt_3 +=1
            if cnt_3 ==5:
                count+=1

    cnt_4 = 0
    for i in range(5):
        if visited[i][4-i] ==True: #역대각
            cnt_4+=1
            if cnt_4 == 5:
                count+=1
    return count

for i in range(len(numbers)):
    find(numbers[i])
    if bingo() == 3:
        print(i+1)#번호는 인덱스+1임
        break




