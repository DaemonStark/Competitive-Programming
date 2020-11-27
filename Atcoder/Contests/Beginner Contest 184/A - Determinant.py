arr = [[j for j in input.strip().split(" ")] for i in range(2)]

determinant = (arr[0] * arr[3]) - (arr[1] * arr[2])
print(determinant)
