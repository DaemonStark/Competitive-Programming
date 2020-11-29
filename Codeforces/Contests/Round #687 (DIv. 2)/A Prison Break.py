def prisonbreak(n, m, r, c):
    distance = (max(r-1, n-r) + max(c-1, m-c))
    return distance


if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        n, m, r, c = map(int, input().split())
        print(prisonbreak(n, m, r, c))
