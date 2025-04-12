import sys
sys.stdin = open('input.txt','r')
#########################################
def gaseo(N,M,arr):
    dic=[(0,1),(0,-1),(1,0),(-1,0)]
    for i in range(N):
        for j in range(N):
            temp = arr[i][j]
            for nx,ny in dic:
                for k in range(1,M):
                    ni= i+nx*k
                    nj= j+ny*k
                    if not(0<=ni<N and 0<=nj<N):
                        continue
                    temp+=arr[ni][nj]
                stack.append(temp)
def dae(N,M,arr):
    dic=[(1,1),(-1,-1),(1,-1),(-1,1)]
    for i in range(N):
        for j in range(N):
            temp = arr[i][j]
            for nx,ny in dic:
                for k in range(1,M):
                    ni= i+nx*k
                    nj= j+ny*k
                    if not(0<=ni<N and 0<=nj<N):
                        continue
                    temp+=arr[ni][nj]
                stack.append(temp)
T = int(input()) # test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    stack=[]
    result_1 = gaseo(N,M,arr)
    result_2 = dae(N,M,arr)

    print(f"#{tc} {max(stack)}")