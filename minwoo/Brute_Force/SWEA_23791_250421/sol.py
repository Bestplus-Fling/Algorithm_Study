import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    player = ['']*N
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    idx_a, idx_b = 0, 0

    for i in range(N):
        # 이미 선발되었다면 다음 선수를 뽑는다.
        while idx_a < N:
            if player[a[idx_a]-1] == '':
                player[a[idx_a] - 1] = 'A'
                idx_a += 1
                break
            idx_a += 1
        while idx_b < N:
            if player[b[idx_b]-1] == '':
                player[b[idx_b] - 1] = 'B'
                idx_b += 1
                break
            idx_b += 1
    print(''.join(player))

