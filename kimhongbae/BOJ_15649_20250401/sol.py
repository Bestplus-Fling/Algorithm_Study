import sys
sys.stdin = open('input.txt','r')

def comb(num,M):
    result = []
    if M == 1:
        return [[i] for i in num]

    for i in range(len(num)):
        elem = num[i]
        for rest in comb(num[:i] + num[i+1:],M - 1):
            result.append([elem] + rest)

    return result

N ,M = map(int,input().split())

num = []
for i in range(1,N+1):
    num.append(i)
ans = comb(num,M)
for k in ans:
    print(*k)