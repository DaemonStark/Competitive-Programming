n = int(input())
lst = list(map(int, input().split()))
length = len(lst)
final_lst = []
for i in range(0, len(lst)):
    friend1 = int(lst[i])
    print("friend1", friend1, end=' ')

    if len(lst) > lst[friend1]:
        lst.append(lst)

    friend2 = int(lst[friend1])
    print("friend2", friend2)

    final_lst.append(friend2)


print(final_lst)
