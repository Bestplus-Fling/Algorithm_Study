a = 0
N = 4
print(''.join(['0' if 1 != N-i else '1' for i in range(N)]))
b = int(''.join(['0' if 1 != N-i else '1' for i in range(N)]), 2)

c = bin(a | b)

print(c)
print(a)
print(b)