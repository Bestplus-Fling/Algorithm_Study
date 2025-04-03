import sys
sys.stdin = open('input.txt','r')

def comb(n, m):
    stack = [(0, [])]
    result = []

    while stack:
        idx, current = stack.pop()

        if len(current) == m:
            result.append(current)
            continue

        for i in range(idx, n):
            stack.append((i + 1, current + [i + 1]))

    return result


n, m = map(int,input().split())


ans = sorted(comb(n,m))
# print(ans)
for k in ans:
    print(*k)
