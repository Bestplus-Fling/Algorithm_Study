import sys
sys.stdin = open('input.txt', 'r')
#########################################

'''
G : 이동 가능한 땅
T : 이동 불가능한 나무
X : 현재 RC카의 위치
Y : RC 카를 이동시키고자 하는 위치


동작
A : 앞으로 이동 - 나무나 필드를 벗어나는 경우 아무일도 일어나지 않는다
L : 현재 바라보고 있는 방향에서 왼쪽으로 90도 회전
R : 현재 바라보고 있는 방향에서 오른쪽으로 90도 회전
'''


def x():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                return i, j


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    q = int(input())
    result = []
    for _ in range(q):
        c, commend = map(str,input().split())
        idx = 0
        i, j = x()
        for k in commend:
            if k == 'R':
                idx += 1
                if idx == 4:
                    idx = 0
            elif k == 'L':
                idx -= 1
                if idx == -1:
                    idx = 3
            else:
                ni = i + dx[idx]
                nj = j + dy[idx]

                if not(0 <= ni < n and 0 <= nj < n):
                    continue

                if arr[ni][nj] == 'T':
                    continue

                i, j = ni, nj

        if arr[i][j] == 'Y':
            result.append(1)
        else:
            result.append(0)

    print(f'#{tc}', *result)



