import sys
sys.stdin = open('input.txt', 'r')


def f(depth, last, num_list):
    global ans, N, M
    if depth == M:
        ans.append(' '.join(num_list))
        return
    for i in range(last, N):
        f(depth+1, i, num_list+f'{i+1}')


N, M = map(int, input().split())
ans = []
f(0, 0, '')
print('\n'.join(map(str, ans)))
