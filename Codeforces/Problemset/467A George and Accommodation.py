n = int(input())
flag = 0
count = 0
for i in range(n):
    p,q = map(int, input().split())
    if p >= q:
        flag = 0
    elif p < q:
        if(q - p >= 2):
            flag = 1
            count += 1

print(count)

