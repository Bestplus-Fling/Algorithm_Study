import sys
sys.stdin = open('input.txt','r')
#########################################


N = int(input())
arr = [list(input().strip()) for _ in range(N)]

dic=[(1,0),(-1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
cnt=0
for i in range(N):
    for j in range(N):
        # 만약 M 을찾았으면
        if arr[i][j] =='M':
            #좌표 이동
            for dx,dy in dic:
                nx=i+dx
                ny=j+dy
                # 만약 범위 안이고 '0'이면 그경로 한번더이동
                if (0<= nx<N and 0<=ny<N) and arr[nx][ny] == 'O':
                    nx+=dx
                    ny+=dy
                    # 만약 범위 안이고 'B'이면 그경로 한번더이동
                    if (0<= nx<N and 0<=ny<N) and arr[nx][ny] == 'B':
                        nx += dx
                        ny += dy
                        # 만약 범위 안이고 'I'이면 그경로 한번더이동
                        if (0<= nx<N and 0<=ny<N) and arr[nx][ny] == 'I':
                            nx += dx
                            ny += dy
                            # 만약 범위 안이고 'S'이면 그경로 한번더이동
                            if (0<= nx<N and 0<=ny<N) and  arr[nx][ny] == 'S':
                                #여기 까지오면 cnt +1 하기
                                cnt+=1

print(cnt)