testcases = int(input())
for i in range(testcases):
    N, X = map(int, input().split(" "))
    A = list(map(int, input().split(" ", maxsplit=N+1)))
    result = []
    tmp = []
    for j in range(len(A)):
        if (X < A[j]):
            t = A.pop(0)
            nxt = X - t
            A.append(nxt)
        elif (X == A[j]):
            A.pop(0)
            A.append(0)
            tmp.append(j+1)
        elif(X > A[j]):
            A.pop(0)
            A.append(0)
            tmp.append(j+1)
    print("Case #{}: {}".format(i+1, tmp))
    tmp.clear()
   