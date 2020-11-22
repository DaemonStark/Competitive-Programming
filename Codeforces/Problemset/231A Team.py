n = int(input())
count = 0
for i in range(n):
    c = list(input())
    no_of_1s = 0
    for each in c:
        if each == '1':
            no_of_1s = no_of_1s + 1    

    if no_of_1s >= 2:
        count = count + 1

print(count)