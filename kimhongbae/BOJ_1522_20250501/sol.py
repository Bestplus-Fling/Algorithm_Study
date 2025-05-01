import sys
sys.stdin = open('input.txt','r')

arr = input()
a = arr.count('a')

arr += arr[0:a-1]
cnt = float('inf')
for i in range(len(arr)-a+1):
    cnt = min(cnt,arr[i:i+a].count('b'))

print(cnt)