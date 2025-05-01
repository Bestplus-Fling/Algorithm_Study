import sys
sys.stdin = open('input.txt','r')
#########################################
n=int(input())
#만약 n은 1이면 그냥 1만 출력
if n ==1:
    print(1)
#만약 1이 아니면
elif n !=1:
    # 초기 더한값
    sum = 0
    #카운트
    cnt = 0

    # 1부터 n까지 순회
    for i in range(1, n + 1):
        # 계속 i값들을 더함
        sum += i
        #만약 합산값이 n보다 커지면
        if sum > n:
            #멈춤
            break
            #더한걸 카운트함
        cnt += 1
    print(cnt)







