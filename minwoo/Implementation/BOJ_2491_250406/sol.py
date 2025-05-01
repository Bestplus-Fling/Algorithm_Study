import sys
sys.stdin = open('input4.txt', 'r')


def f(start, end, increase):
    global result
    case = 0
    for i in range(start, end, increase):
        if D[i] <= D[i + increase]:
            case += 1
        else:
            result = max(result, case + 1)
            case = 0
    result = max(result, case + 1)


N = int(input())
D = list(map(int, sys.stdin.readline().split()))
result = 0
f(0, N-1, 1)
f(N-1, 0, -1)
print(result)
