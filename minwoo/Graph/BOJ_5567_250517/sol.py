import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def f():
    global graph
    queue = [1]
    depth = 1
    guest = 0
    visited = [0] * (N+1)
    visited[1] = 1
    while depth < 3 and queue:
        temp = []
        for vertex in queue:
            for adj in graph[vertex]:
                if visited[adj] == 1: continue
                visited[adj] = 1
                guest += 1
                temp.append(adj)
        queue = temp
        depth += 1
    return guest


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(f())