s = str(input())
countu = 0
countl = 0

for each in s:
    if each.isupper() == True:
        countu += 1
    else:
        countl += 1
    
if countu > countl:
    print(s.upper())
elif countl > countu:
    print(s.lower())
else:
    print(s.lower())

