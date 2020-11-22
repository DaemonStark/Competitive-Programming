n = int(input())
ls = []
for i in range(n):
    s = input()
    l = str(len(s) - 2)
    if len(s) > 10:
        ls.append(s[0] + l + s[-1])
    else:
        ls.append(s)

for each in ls:
    print(each, end='\n')
