k, n, w = map(int, input().split(" "))
amount = 0
for i in range(w):
    amount = amount +  (i + 1) * k
    
if(amount - n > 0):
    print(amount - n)
else:
    print(0)

