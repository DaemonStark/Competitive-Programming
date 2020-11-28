a, b, x, y = map(int, input().split())
time = 0
if a > b:
    a -= 1

time += x
time += abs(a-b) * min(y, 2*x)
print(time)
