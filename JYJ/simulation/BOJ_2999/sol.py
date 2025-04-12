import sys
sys.stdin = open('input.txt', 'r')
#########################################

'''
r <= C 이고 r*c = n 인 r과 c를 고른다
그러한 경우가 여러 개일 경우 r이 큰 값을 선택한다

그 다음 행이 r개고 열이 c 개인 행렬을 만든다

행렬에 모두 메시지를 옮겼다면, 이 것을 첫 번째 열의 첫 번째 행부터
r 번째 행 까지 차례대로 읽으면서 받아적는다

'''
def rnc(): # 조건에 맞는 r과 c를 찾는 함수
    r = c = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i <= j and i * j == n:
                if r < i:
                    r, c = i, j
    return r, c


word = list(input())
n = len(word)
r, c = rnc()
idx = 0
arr = [[''] * r for _ in range(c)]
result = []

for i in range(c): # 하나씩 배열에 추가
    for j in range(r):
        arr[i][j] = word[idx]
        idx += 1

# print(arr)

for i in range(r): # 배열 다시 읽기
    for j in range(c):
        result.append(arr[j][i])

for i in result:
    print(''.join(i), end='')



