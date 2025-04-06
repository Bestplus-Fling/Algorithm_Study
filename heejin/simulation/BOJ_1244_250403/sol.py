import sys
sys.stdin = open("input.txt", "r")

N = int(input())
switch = list(map(int, input().split()))
student = int(input())
for i in range(student):
    s, c = map(int, input().split())

    if s == 1:
        for j in range(c-1, N , c):
            switch[j] = 1-switch[i]

    else:
        c-=1
        l , r = c,c

        while l > 0 and r < N-1 and switch[l-1]==switch[r+1]:
            l -=1
            r +=1

        for j in range(l,r+1):
            switch[j]=1-switch[j]

print(*switch)
