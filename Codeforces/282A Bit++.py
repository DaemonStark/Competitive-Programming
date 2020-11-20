n = int(input())
x = 0
for i in range(n):
    op = input()
    x = x + (-1 if '-' in op else 1)

print(x)