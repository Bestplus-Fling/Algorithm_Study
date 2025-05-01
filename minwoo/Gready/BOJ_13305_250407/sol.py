import sys
sys.stdin = open("input.txt", "r")

N = int(input())
road = list(map(int, sys.stdin.readline().split()))
station = list(map(int, sys.stdin.readline().split()))
result = station[0] * road[0]
min_cost = station[0]
for i in range(1, N-1):
    if min_cost > station[i]:
        min_cost = station[i]
    result += (min_cost * road[i])
print(result)
