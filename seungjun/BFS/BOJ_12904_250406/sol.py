import sys
sys.stdin = open('input.txt', 'r')
######################################
import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

start_len = len(s)
target_len = len(t)

visited = set()
result = 0
# 시작 문자 s의 길이
stack = [(t, target_len)]

while stack:
    now, length = stack.pop()

    if length < start_len:
        continue

    if now == s:
        result = 1
        break

    if now[-1] == 'A':
        stack.append((now[:-1], length - 1))

    if now[-1] == 'B':
        stack.append((now[:-1][::-1], length - 1))

print(result)