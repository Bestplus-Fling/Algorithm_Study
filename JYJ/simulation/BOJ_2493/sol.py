import sys
sys.stdin = open('input.txt', 'r')
#########################################
import sys
input = sys.stdin.readline

'''

'''
n = int(input())
arr = list(map(int,input().split()))

result = [0] * n
stack = []

for i in range(n):
    while stack and stack[-1][0] < arr[i]:
        stack.pop()  # 자신보다 작은 건 의미 없음

    if stack:
        result[i] = stack[-1][1]  # 가장 가까운 큰 수의 인덱스
    else:
        result[i] = 0  # 왼쪽에 자신보다 큰 수가 없음

    stack.append((arr[i], i + 1))  # 현재 값과 위치 저장

print(*result)



