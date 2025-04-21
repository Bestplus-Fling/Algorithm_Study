import sys
sys.stdin = open('input.txt', 'r')


def f():
    global carrot, K, N
    case = N // 2
    ans = float('inf')
    for i in range(K):
        for j in range(i+1, K):
            a, b, c = sum(carrot[:i]), sum(carrot[i:j]), sum(carrot[j:])
            temp = [a, b, c]
            if 0 in temp:
                continue
            if case < a or case < b or case < c:
                continue
            ans = min(max(temp) - min(temp), ans)
    if ans == float('inf'):
        return -1
    return ans


T = int(input())
K = 31
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    carrot = [0] * K
    for p in arr:
        carrot[p] += 1
    print(f'#{tc}', f())
