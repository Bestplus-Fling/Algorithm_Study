'''
평면에 네 개의 직사각형이 놓여 있는데 그 밑변은 모두 가로축에 평행하다. 이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고, 겹쳐 있을 수도 있고, 하나가 다른 하나를 포함할 수도 있으며, 변이나 꼭짓점이 겹칠 수도 있다.

이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.
'''
import sys
sys.stdin = open('input.txt', 'r')
#########################################

arr=[[0]*100 for _ in range(100)]
for i in range(4):
    left_x,left_y,right_x,right_y=map(int,input().split())
    for x in range(left_x,right_x):
        for y in range(left_y,right_y):
            arr[x][y]=1
cnt = 0
for check in arr:
    for real in check:
        if real==1:
            cnt+=1
print(cnt)#26