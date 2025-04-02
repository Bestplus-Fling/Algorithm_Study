import sys
sys.stdin = open('input1.txt', 'r')

N = int(input())
sims = [0]
graph = [[] for _ in range(N+1)]
sims.extend(list(map(int, input().split())))

for i in range(N):
    n, *arr = map(int, input().split())
    graph[i+1] = arr
print(graph)
