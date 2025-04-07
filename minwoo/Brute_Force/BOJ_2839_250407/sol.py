N = int(input())

kg5, now = divmod(N, 5)
kg3 = 0
ans = -1
while kg5 >= 0:
    if now % 3 != 0:
        kg5 -= 1
        now += 5
    else:
        ans = kg5 + (now // 3)
        break
print(ans)
