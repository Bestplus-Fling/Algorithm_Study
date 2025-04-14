import sys
sys.stdin = open('input.txt','r')
#########################################
N = int(input())
a_arr = list(map(int,input().split()))
b_arr = list(map(int,input().split()))

result=0
a_arr.sort()
b_arr.sort(reverse=True)
for i in range(N):
    result+=a_arr[i]*b_arr[i]
print(result)
