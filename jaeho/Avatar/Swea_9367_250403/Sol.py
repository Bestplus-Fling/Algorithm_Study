import sys
sys.stdin = open('input.txt','r')
#########################################

T = int(input()) # test case 개수를 받아오는 코드
for tc in range(1, T+1):
    arr_len = int(input())   #N: 양의 정수 개수
    arr = list(map(int,input().split()))
    result=1
    cnt = 1
    for i in range(arr_len-1):
        if arr[i]<arr[i+1]:
            cnt+=1
            if cnt>result:
                result=cnt
        else:
            cnt=1

    print(f"#{tc} {result}")
