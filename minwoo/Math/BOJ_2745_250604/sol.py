import sys
sys.stdin = open('input.txt', 'r')

N, B = input().split()
B = int(B)
print(int(N, B))