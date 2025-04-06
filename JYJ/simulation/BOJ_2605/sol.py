import sys
sys.stdin = open('input.txt', 'r')
#########################################

'''

첫 번쨰로 줄을 선 학생은 무조건 0번
두 번째로 줄을 선 학생은 0번 또는 1번 둘 중 하나

0번을 뽑으면 그 자리에 그대로 있고, 1번을 뽑으면 바로 앞의 학생 앞으로 가서 줄을 선다

세 번째로 줄을 선 학생을 0, 1 또는 2 중 하나의 번호를 뽑는다
그리고 뽑은 번호만큼 앞자리로 가서 줄을 선다

'''


n = int(input())

nums = list(map(int,input().split()))


result = []

for i in range(n):
    result.append(i + 1)
    move = nums[i]
    for j in range(move):
        result[-(j + 2)], result[-(j + 1)] = result[-(j + 1)], result[-(j + 2)]
        # 뒤에서 두 번째랑 마지막이랑 계속 바꿔치기

print(*result)





