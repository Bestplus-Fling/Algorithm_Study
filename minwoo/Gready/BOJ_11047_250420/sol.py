import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def count(now):
    global coin, N
    cnt = 0
    idx = 0
    while now > 0:
        if now // coin[idx] > 0:
            c, now = divmod(now, coin[idx])
            cnt += c
        idx += 1
    return cnt


N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
coin.reverse()
print(count(K))
