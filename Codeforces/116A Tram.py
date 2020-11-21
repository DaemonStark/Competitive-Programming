def tram(n):
    no_of_passengers_inside_the_tram = 0
    capacity = 0
    for i in range(n):
        a, b = map(int, input().split())
        no_of_passengers_inside_the_tram -= a
        no_of_passengers_inside_the_tram += b
        capacity = max(capacity, no_of_passengers_inside_the_tram)

    return capacity


if __name__ == '__main__':
    n = int(input())
    print(tram(n))
