import sys
sys.stdin = open('input.txt', 'r')


"""
1번부터 N번까지 N개의 상자
처음에는 모두 0

다음 Q회동안 일정 범위의 연속한 상자를 동일한 숫자로 변경하고자 한다

i( 1 <= i <= Q)번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경
"""


T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = ['0'] * N
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            box[j] = str(i+1)
    print(f'#{tc}', ' '.join(box))

