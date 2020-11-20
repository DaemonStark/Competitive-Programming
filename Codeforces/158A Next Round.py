n, k  = map(int, input().split())
a = list(input().split())
advanced =[]
for i in range(0,len(a)):
    if int(a[i]) >= int(a[k-1]) and int(a[i]) > 0 :
        advanced.append(a[i])

print(len(advanced))
