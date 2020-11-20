n = int(input())
st = input()
# count the min no of stones to take from the table so that any two neighb stones had diff colors

count = 0
for i in range(n-1):
    if(st[i] == st[i+1]):
        count = count + 1

print(count)