n = int(input())
count = 1
mag = []
for j in range(n):
    mag.append(input())

for i in range(1, len(mag)):
    if mag[i] == mag[i-1]:
        count += 0
    else:
        count += 1

print(count)
