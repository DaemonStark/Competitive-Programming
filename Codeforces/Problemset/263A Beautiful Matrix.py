for i in range(5):
    arr =[int(x) for x in input().split()]
    for j in range(5):
        if arr[j] == 1:
            a = (abs(2 - i) + abs(2 - j))
            exit
    
print(a)