def wrongsub(n, k):
    for i in range(k):
        last_digit = int(n % 10)
        if last_digit == 0:
            n = int(n/10)
        else:
            n -= 1

    return n


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(wrongsub(n, k))
