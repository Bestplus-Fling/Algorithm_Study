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

        for i in range(n):
            stack.append((i+1, current + [i + 1]))

    return result


n, m = map(int,input().split())


ans = sorted(comb(n,m))
# print(ans)
for k in ans:
    print(*k)
# def comb(x):
#
#     if x == n:
#         return
#
#     a = arr[x]
#
#     for i in range(x+1,n+1):
#         b = i
#         result.append([a,b])
#     comb(x+1)
#
#
#
# n, m = map(int,input().split())
#
# arr = [i for i in range(1,n+1)]
# result = []
# comb(0)
# # print(arr)
# if m == 1:
#     for i in range(1,n+1):
#         print(i)
# else:
#     for k in result:
#         print(*k)