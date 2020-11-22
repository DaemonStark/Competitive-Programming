n = int(input()) # Quantity of friends petya invited
a = int(input().split(" ")) # ith no. is Pi, the number of a fr who gave a gift too fr no. i

# need to print n space sep int : ith no. should equal the no. of the fr who gave a gift to fr no. i
# i.e for the given input like this 
# 4             no. of friends
# 2 3 4 1       numbers
# 0 1 2 3       indexes
# 1 2 3 4       numbering of friends according to petya
# 4 1 2 3       answer
# 1st(0th index) number friend gave gift to (2) number fr so 
# in answer the number of that friend should come at that (i+1)th place
# the code will be as down below

tlist = []

for i in range(n):
    temp = a[i]
    tlist.append(a[temp])

for j in tlist:
    print(tlist[j], end=' ')


# n, p, d = input(), map(int, raw_input().split()), {}

# for i, v in enumerate(p):
#     d[v] = i + 1
# for i in xrange(n):
#     print d[i+1],