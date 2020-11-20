a, b = map(int, input().split())
count = 1
while True:
    a = a * 3
    b = b * 2 
    if a > b:
        print(count)
        break
    else:
        count += 1

