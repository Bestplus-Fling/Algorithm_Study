import sys
sys.stdin = open("input.txt", "r")

from itertools import combinations

hi = []

for _ in range(9):
    hi.append(int(input()))


for com in combinations(hi, 7):
    if sum(com) == 100:
        for small in sorted(com):
            print(small)
        break
