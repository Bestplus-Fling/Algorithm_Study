import sys
sys.stdin = open('input.txt', 'r')
#########################################

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def jari(i, j):
    idx = 0
    cnt = 1
    arr[i][j] = 1
    while True:
        if cnt == k: # 대기번호 k인 손님 찾기
            re, sult = i + 1, j + 1
            break

        ni = i + dxy[idx][0]
        nj = j + dxy[idx][1]

        if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] == 0:
            arr[ni][nj] = 1
            cnt += 1
            i, j = ni, nj
        else:
            idx = (idx + 1) % 4
    return re, sult


c, r = map(int,input().split())
k = int(input())
arr = [[0] * c for _ in range(r)]

if c * r < k: # 배열에서 나올 수 있는 수보다 크면 그냥 프린트 0 찍기
    print(0)
else:
    i, j = jari(0,0)
    print(j, i)


