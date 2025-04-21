import sys
sys.stdin = open('input.txt', 'r')
a, b, c = map(int, sys.stdin.readline().split())


def f(x, n):
    if n == 1:
        return x % c
    if n % 2 == 0:
        y = f(x, n // 2)
        return (y * y) % c
    else:
        y = f(x, (n-1) // 2)
        return (y * y * x) % c


print(f(a, b) % c)

