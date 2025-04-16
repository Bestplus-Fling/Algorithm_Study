import sys
sys.stdin = open("input.txt", "r")
from collections import deque
dic = {
    (1, 3): (3, 1, 3, 1),
    (2, 4): (4, 2, 4, 2),
    (1, 4): (1, 4, 1, 4),
    (2, 3): (2, 3, 2, 3)
}

N = 6
K = int(input())
queue = deque([list(map(int, input().split())) for _ in range(N)])
num = [0] * 4
idx = []
for q in queue:
    num[q[0]-1] += 1
    if num[q[0]-1] > 1:
        idx.append(q[0])
idx.sort()
tpl = (idx[0], idx[1])
a, b, c, d = dic[tpl]
while True:
    if a == queue[0][0] and b == queue[1][0] and c == queue[2][0] and d == queue[3][0]:
        break
    queue.rotate(1)
big = (queue[0][1]+queue[2][1]) * (queue[1][1]+queue[3][1])
small = queue[1][1] * queue[2][1]
print((big - small) * K)
