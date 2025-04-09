import sys
sys.stdin = open('input.txt', 'r')
#########################################

n=input().strip()
result=''
for i in n:
    if i not in 'CAMBRIDGE':
        result+=i
print(result)


