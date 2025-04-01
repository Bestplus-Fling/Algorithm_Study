import sys
sys.stdin = open("input.txt", "r")


N, M = map(int, input().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(*data, sep='\n')

"""
0: temp
1: floor
2: virus
"""
# 1.