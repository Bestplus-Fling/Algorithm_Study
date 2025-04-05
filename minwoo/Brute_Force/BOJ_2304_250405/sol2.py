import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
data = sorted([tuple(map(int, input().split())) for _ in range(N)])
P = [0] * (data[-1][0]+1)
forward_sum, reverse_sum = 0, 0
max_idx, max_val = -1, -1
for i in range(N):
    if max_val < data[i][1]:
        max_idx = i
        max_val = data[i][1]


def install(start, end, increase, length):
    for k in range(start, end, increase):
        P[k] = length


# 정방향으로 가다가 가장 큰 기둥을 만나면 종료
for i in range(max_idx):
    if P[data[i][0]]: continue
    for j in range(i+1, max_idx):
        if data[i][1] < data[j][1]:
            ni = j
            break
    else:
        install(data[i][0], data[max_idx][0], 1, data[i][1])
        continue
    install(data[i][0], data[ni][0], 1, data[i][1])

# 역방향으로 가다가 가장 큰 기둥을 만나면 종료
for i in range(N-1, max_idx, -1):
    if P[data[i][0]]: continue
    for j in range(i-1, max_idx, -1):
        if data[i][1] < data[j][1]:
            ni = j
            break
    else:
        install(data[i][0], data[max_idx][0], -1, data[i][1])
        continue
    install(data[i][0], data[ni][0], -1, data[i][1])
# 마지막으로 가장 큰 기둥값을 더한다.
P[data[max_idx][0]] = max_val
print(sum(P))