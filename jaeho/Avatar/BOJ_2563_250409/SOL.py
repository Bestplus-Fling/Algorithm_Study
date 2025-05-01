import sys
sys.stdin = open('input.txt','r')
#########################################

Paper_gaesu=int(input())
arr = [[0] * 101 for _ in range(101)]
for _ in range(Paper_gaesu):
    x,y=map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j]=1

result=0
for i in arr:
    for j in i:
        if j == 1:
            result+=1
print(result)