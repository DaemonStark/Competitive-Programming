t = int(input())
for i in range(1, t + 1):
    n = int(input())
    if(n == 1):
        print(0)
    elif(n == 2):
        print(1)
    elif(n == 3 or n % 2 == 0):
        print(2)
    else:
        print(3)
