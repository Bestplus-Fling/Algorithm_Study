import sys
sys.stdin = open('input.txt','r')
#########################################
arr = list(input().strip())
n = len(arr)
cnt = 0
for i in range(n):
    if arr[i] == 'Y':  # i+1번 스위치를 눌러야 함
        # i 이후부터 배수위치만 반전시켜야함
        for j in range(i, n, i + 1):  # (i+1)의 배수 위치 반전
            if arr[j] == 'Y':
                arr[j] = 'N'
            else:
                arr[j] = 'Y'
        # 일단 y이면 꺼야되니 cnt+1
        cnt += 1

cnt_2=0
for a in arr:
    for b in a:
        if b == 'N':
            cnt_2+=1
if cnt_2 == len(arr):
    print(cnt)
else:
    print(-1)
# 이렇게 간단한 방법도 있음
# # 결과 확인
# if all(c == 'N' for c in arr):
#     print(cnt)
# else:
#     print(-1)
#
