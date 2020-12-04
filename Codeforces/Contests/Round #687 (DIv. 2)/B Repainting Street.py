def repaint(nlist, k):
    count = 0

    for i in range(1, 101):
        for j in range(1, len(nlist)):
            if nlist[j] != i:
                j = j+k-1
                count += 1

    return count


if __name__ == '__main__':
    t = int(input())
    nlist = []
    for i in range(0, t):
        n, k = map(int, input().split())
        nlist = input().split()[:n]
        print(repaint(nlist, k))
