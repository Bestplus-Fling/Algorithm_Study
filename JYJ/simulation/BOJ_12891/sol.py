import sys
sys.stdin = open('input.txt', 'r')
#########################################
#
# from collections import deque
# import sys
# input = sys.stdin.readline
'''
배열에서 p개씩 슬라이싱
DNA 리스트에 있는지 없는지 검사
주어진 문자의 최소 개수가 맞는지 검사
조건에 맞는 사용할 수 있는 비밀번호의 개수 출력
'''

# DNA = ['A', 'C', 'G', 'T']
# s, p = map(int,input().split())
# arr = list(input().strip())
# A, C, G, T = map(int,input().split())
# words = deque(arr[:p])
# cnt = 0
# idx = p
# while True:
#     if idx >= s + 1:
#         break
#     a_count = 0
#     c_count = 0
#     g_count = 0
#     t_count = 0
#     # print(words)
#     for j in words:
#         if j == 'A':
#             a_count += 1
#         elif j == 'C':
#             c_count += 1
#         elif j == 'G':
#             g_count += 1
#         elif j == 'T':
#             t_count += 1
#
#     if a_count == A and c_count == C and g_count == G and t_count == T:
#         cnt += 1
#     words.popleft()
#     if idx < s:
#         words.append(arr[idx])
#     idx += 1
#
# print(cnt)

import sys
input = sys.stdin.readline

s, p = map(int, input().split())
arr = list(input().strip())
A_target, C_target, G_target, T_target = map(int, input().split())

# 현재 윈도우 내 문자 개수 카운팅용
a_count = 0
c_count = 0
g_count = 0
t_count = 0

# 초기 윈도우 설정
for i in range(p):
    if arr[i] == 'A':
        a_count += 1
    elif arr[i] == 'C':
        c_count += 1
    elif arr[i] == 'G':
        g_count += 1
    elif arr[i] == 'T':
        t_count += 1

cnt = 0
# 첫 윈도우 검사
if a_count >= A_target and c_count >= C_target and g_count >= G_target and t_count >= T_target:
    cnt += 1

# 슬라이딩 윈도우 시작
for i in range(p, s):
    # 나가는 문자
    out_char = arr[i - p]
    if out_char == 'A':
        a_count -= 1
    elif out_char == 'C':
        c_count -= 1
    elif out_char == 'G':
        g_count -= 1
    elif out_char == 'T':
        t_count -= 1

    # 들어오는 문자
    in_char = arr[i]
    if in_char == 'A':
        a_count += 1
    elif in_char == 'C':
        c_count += 1
    elif in_char == 'G':
        g_count += 1
    elif in_char == 'T':
        t_count += 1

    # 검사
    if a_count >= A_target and c_count >= C_target and g_count >= G_target and t_count >= T_target:
        cnt += 1

print(cnt)


