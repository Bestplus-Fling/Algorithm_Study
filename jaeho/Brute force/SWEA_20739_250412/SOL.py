import sys
sys.stdin = open('input.txt','r')
#########################################

T = int(input()) # test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N,M = map(int,input().split())   #N: 양의 정수 개수
    arr=[list(map(int,input().split())) for _ in range(N)]

    # 가로
    max_val_1 = 0

    for i in range(N):
        cnt_1 = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt_1 += 1
                if cnt_1 > max_val_1:
                    max_val_1 = cnt_1
            else:
                cnt_1 = 0

    max_val_2 = 0

    for i in range(M):
        cnt_2 = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt_2 += 1
                if cnt_2 > max_val_2:
                    max_val_2 = cnt_2
            else:
                cnt_2 = 0
    if max_val_2 == 1 and max_val_1 == 1:
        print(f"#{tc} {0}")
    else:
        print(f"#{tc} {max(max_val_1, max_val_2)}")