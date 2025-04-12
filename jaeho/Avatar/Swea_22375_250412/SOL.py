import sys
sys.stdin = open('input.txt','r')
#########################################

T = int(input()) # test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())   #N: 양의 정수 개수
    start_switch = list(map(int,input().split()))
    target_switch = list(map(int, input().split()))
    result=0
    for i in range(N):
        #만약 현재값이 목표 스위치와 다르면
        if start_switch[i] != target_switch[i]:
            #i 부터 길이끝까지
            for j in range(i,N):
                #스타트위치를 0은 1로 1은 0으로 바꿈
                start_switch[j]=1-start_switch[j]
            result+=1



    print(f"#{tc} {result}")
