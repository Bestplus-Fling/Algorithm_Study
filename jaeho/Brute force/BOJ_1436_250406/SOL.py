import sys
sys.stdin = open('input.txt','r')
#########################################

n=int(input())
num=0
#1부터 10001까지 순회
for movie_name_num in range(1,10000000):
    #만약 i안에 666이 있으면
    if '666' in str(movie_name_num):
        #num 카운트 하기
        num+=1
        # 만약 넘버와 값이 주어진 정수 값과 같아지면 i출력
        if num == n:
            print(movie_name_num)
            break



