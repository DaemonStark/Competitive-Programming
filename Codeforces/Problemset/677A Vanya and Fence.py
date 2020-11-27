n, h = map(int, input().split())
arr = map(int, input().split())

for each in arr:
    if each > h:
        n += 1

print(n)
