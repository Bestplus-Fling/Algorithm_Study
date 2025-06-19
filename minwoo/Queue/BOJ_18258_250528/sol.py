import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
queue = deque()
for n in range(N):
    cmd = list(input().split())
    # print(cmd)
    if (acc:=cmd[0]) == 'push':
        queue.append(cmd[1])
    elif acc == 'pop':
        print(queue.popleft() if queue else -1)
    elif acc == 'size':
        print(len(queue))
    elif acc == 'empty':
        print(0 if queue else 1)
    elif acc == 'front':
        print(queue[0] if queue else -1)
    else:
        print(queue[-1] if queue else -1)

