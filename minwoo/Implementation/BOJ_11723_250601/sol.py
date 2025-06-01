import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
"""
총 20자리의 비트가 있음
이 비트는 각 자리를 의미
따라서 x라는 숫자가 입력되면 x번째의 비트가 1이 되는 형태
이렇게 하기 위해서는 2**x 자리의 비트가 1이 되야 함
"""

M = int(input())
union = 0
for _ in range(M):
    cmd = list(input().split())
    if (c := cmd[0]) not in ['all', 'empty']:
        num = int(cmd[1])
        if c == 'add':
            union |= (1 << num)
        elif c == 'remove':
            union &= ~(1 << num)
        elif c == 'check':
            print('1' if union & (1 << num) else '0')
        elif c == 'toggle':
            union ^= (1 << num)
    else:
        if c == 'all':
            union |= (1 << 21) - 1
        elif c == 'empty':
            union = 0
# print('\n'.join(ans))

# for i, t in enumerate("""1101010101100010"""):
#     print(i, 'P' if ans[i] == t else 'F')