n = int(input())
s = str(input()[:n])
alphabet = "abcdefghijklmnopqrstuvwxyz"
flag = 0
for each in s.lower():
    if each not in alphabet:
        flag = 1
    else:
        flag = 0

if flag == 1:
    print("YES")
else:
    print("NO")

# flag = 0
# for each in alphabet:
#     if each not in s.lower():
#         flag = 0
#     else:
#         flag = 1
        
# if flag == 0:
#     print("NO")
# else:
#     print("YES")