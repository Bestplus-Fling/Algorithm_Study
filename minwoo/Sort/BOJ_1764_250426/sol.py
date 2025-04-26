import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N, M = map(int, input().split())
listen = set([input().strip() for _ in range(N)])
arr = []
cnt = 0

for person in [input().strip() for _ in range(M)]:
    if person in listen:
        cnt += 1
        arr.append(person)
arr.sort(key=len)
print(cnt, *sorted(arr, key=lambda x: x[::]), sep='\n')
