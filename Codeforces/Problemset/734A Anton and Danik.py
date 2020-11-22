n = int(input())
s = str(input()[:n])
counta = 0
countd = 0
for each in s:
    if each == 'A':
        counta += 1
    elif each == 'D':
        countd += 1

if counta > countd:
    print("Anton")
elif countd > counta:
    print("Danik")
else:
    print("Friendship")