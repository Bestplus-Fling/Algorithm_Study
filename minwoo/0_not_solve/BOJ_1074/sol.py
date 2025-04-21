import sys
sys.stdin = open('input.txt', 'r')


def dfs():
    """
    1. n > 1일 경우 분할
        - 여기서 분할되는 위치를 명확히 해야 함.
    :return:
    """


N, r, c = map(int, input().split())
width = 2 ** N
grid = [[0] * width for _ in range(width)]
k = (width-1) // 2

print(k)