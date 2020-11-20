from math import ceil 
t = int(input())
for test in range(t):
    n,x = list(map(int,input().split()))
    amts = list(map(int,input().split()))
    left = []
    q = [i+1 for i in range(n)]
    # print(q)
    turns = [ceil(i/x) for i in amts]
    ans = zip(*sorted(zip(turns,q)))
    ans = [str(j) for j in [list(i) for i in ans][1]]
    print("Case #{}: {}".format(str(test+1),' '.join(ans)))