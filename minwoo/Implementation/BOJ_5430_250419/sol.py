import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def action():
    global commend, arr, N
    check = 0
    st, ed = 0, N
    for cmd in commend:
        if cmd == 'R':
            check = 1 - check
        elif cmd == 'D':
            if check == 1:
                ed -= 1
            else:
                st += 1
    return st, ed, check


T = int(input())
for tc in range(1, T+1):
    commend = list(input().strip())
    N = int(input())
    arr = list(input().rstrip().strip('[]').split(','))
    if commend.count('D') > N:
        print('error')
        continue
    s, e, r = action()
    result = arr[s:e]
    if r == 1:
        result.reverse()
    print(f'[{",".join(result)}]')
