a = input()
b = input()

c = [str(int(a[i])^int(b[i])) for i in range(len(a))]
c = ''.join(c)
print(c)