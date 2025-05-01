import sys
sys.stdin = open('input.txt','r')

n = int(input())
arr = sorted(map(int,input().split()))

cnt = []
result = 0
for i in range(n):
    result += sum(cnt) + arr[i]
    cnt.append(arr[i])


print(result)