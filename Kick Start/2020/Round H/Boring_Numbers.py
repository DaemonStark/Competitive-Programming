def boring(l, r):
    lst = []
    # Create the list of that range
    for i in range(l, r):
        lst.append(i)

    # for every integer in the list seperately check the digits for the boring condition
    # boring condition
    # odd at odd index of the number and even at even index of the number
    # Seperate the digits to check
    count = 0
    for j in lst:
        split = [int(k) for k in str(j)]
        for i in range(len(split)-1):
            if split[i] % 2 == split[i+1] % 2:
                count += 0
            else:
                count += 1

    return count


def oddeven_alter(l):
    l = [i % 2 for i in l]
    return all([any([all(l[::2]), all(not i for i in l[::2])]), any([all(l[1::2]), all(not i for i in l[1::2])])]))


if __name__ == "__main__":
    t=int(input())
    for i in range(1, t + 1):
        l, r=map(int, input().split())
        print("Case #{}: {}".format(i, boring(l, r)))
