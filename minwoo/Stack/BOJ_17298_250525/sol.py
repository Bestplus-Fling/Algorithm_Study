import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = []
pop_val = []
while arr:
    num = arr.pop()
    if not pop_val:
        pop_val.append(num)
        result.append(-1)
        continue

    while pop_val and pop_val[-1] <= num:
        pop_val.pop()
    if not pop_val:
        result.append(-1)
    else:
        result.append(pop_val[-1])
    pop_val.append(num)

print(*result[::-1])
