import sys
sys.stdin = open('input.txt','r')
#########################################


n,m= map(int,input().split()) #N: 양의 정수 개수
arr = [list(input().strip()) for _ in range(n)]
garo_stack = []
sero_stack = []
# 가로 # 카운트 해서 넣기
for i in range(n):
    cnt=0
    for j in range(m):
        if arr[i][j] =='#':
            cnt+=1
    garo_stack.append(cnt)
# 세로 # 카운트 해서 넣기
for i in range(m):
    cnt=0
    for j in range(n):
        if arr[j][i] =='#':
            cnt+=1
    sero_stack.append(cnt)
    #내부 0 다지우기
garo=[x for x in garo_stack if x!=0]
sero=[x for x in sero_stack if x!=0]
#만약 가로 스택첫번째 자리 빼기 마지막 꺼 뱄을때 -1이면 up임
if garo[0]-garo[-1] == -1:
    print("UP")
#만약 가로 스택첫번째 자리 빼기 마지막 꺼 뱄을때 1이면 down임
if garo[0]-garo[-1] == 1:
    print("DOWN")

#만약 세로 스택첫번째 자리 빼기 마지막 꺼 뱄을때 -1이면 LEFT임
elif sero[0]-sero[-1] == -1:
    print("LEFT")
#만약 세로 스택첫번째 자리 빼기 마지막 꺼 뱄을때 1이면 Right임
elif sero[0]-sero[-1] == 1:
    print("RIGHT")







