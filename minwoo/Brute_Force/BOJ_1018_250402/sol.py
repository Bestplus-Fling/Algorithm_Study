import sys
sys.stdin = open("input1.txt", "r")

N, M = map(int, input().split())
data = [list(input().strip()) for _ in range(N)]
print(*data, sep='\n')
# 시작위치가 검은색일 경우와 흰색일 경우 정답 배열을 만든다
if data[0][0] == 'B':
    # 짝수행 짝수열은 B, 홀수행 홀수열은 B
    # 홀수행 짝수열은 W, 짝수행 홀수열은 W
    pass
else:
    pass