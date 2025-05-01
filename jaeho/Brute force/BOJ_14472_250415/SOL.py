import sys
sys.stdin = open('input.txt','r')
#########################################

N,M,size=map(int,input().split())
arr=[list(input().strip())for _ in range(N)]

result=0
#가로
for i in range(N):
    cnt = 0
    for j in range(M):
        #만약 .이면 cnt+=1
        if arr[i][j] == '.':
            cnt+=1
            #만약 cnt 값이 size 값과 같아지면 res 에 +1
            if cnt == size:
                result+=1
            #해당 하지않는데 cnt>size 이면 리설트 +1
            elif cnt > size:
                result+=1
            # 해당하지않는데 M이 size 보다 큰데
            elif M>size:
                #cnt값이 M 과같으면
                if cnt == M:
                    #결과값에 m-size 하고 초기화
                    result+=M-size
                    cnt=0
        else:
            cnt=0
#세로
for i in range(M):
    cnt = 0
    for j in range(N):
        if arr[j][i] >= '.':
            cnt+=1
            if cnt == size:
                result += 1
            elif cnt > size:
                result += 1
            elif N > size:
                if cnt == N:
                    result += N - size
                    cnt = 0
        else:
            cnt = 0
print(result)
