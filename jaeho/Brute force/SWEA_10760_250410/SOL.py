import sys
sys.stdin = open('input.txt','r')
#########################################
T = int(input()) # test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    dic=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    jari = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            temp=arr[i][j]
            for dx,dy in dic:
                nx= i+dx
                ny= j+dy
                if not (0<=nx<N and 0<=ny<M):
                    continue
                    #현재값 과 주벼값 비교해서 현재값보다 작은 위치 있으면 카운트 +1
                if temp>arr[nx][ny]:
                    cnt+=1
                    #만약 카운트 체크값이 4가 되면
                    if cnt == 4:
                        #그건 착륙가능자리
                        jari+=1
                        break

    print(f"#{tc} {jari}") #5,6,16