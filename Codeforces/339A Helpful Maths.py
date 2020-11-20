dig = input().split("+")
dig.sort()
l = len(dig)
for i in range(l):
    if(i == l-1):
        print(dig[i])
    else:
        print(dig[i] + "+", end='')
    