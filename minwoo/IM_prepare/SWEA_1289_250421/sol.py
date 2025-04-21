import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    bit = list(map(int, input().strip()))
    N = len(bit)
    case = [0] * N
    cnt = 0
    for i in range(N):
        if bit[i] == case[i]:
            continue
        cnt += 1
        for j in range(i, N):
            case[j] = 1 - case[j]
    print(f'#{tc}', cnt)
