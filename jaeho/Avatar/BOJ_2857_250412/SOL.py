import sys
sys.stdin = open('input.txt','r')
#########################################


arr = [list(input().split()) for _ in range(5)]
stack=[]
for i in range(5):
    for j in arr[i]:
        if "FBI" in j:
            stack.append(i+1)
            break
if stack:
    print(*stack)
else:
    print("HE GOT AWAY!")



