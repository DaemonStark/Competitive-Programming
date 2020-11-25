def elephant(x):
    steps = 0
    steps = int(x/5)
    if(x % 5 != 0):
        steps += 1
    return int(steps)


if __name__ == '__main__':
    x = int(input())
    print(elephant(x))
