import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = sorted(list(map(int, input().split())))
P = [arr[0]]

for i in range(1, N):
    P.append(P[-1] + arr[i])

print(sum(P))
