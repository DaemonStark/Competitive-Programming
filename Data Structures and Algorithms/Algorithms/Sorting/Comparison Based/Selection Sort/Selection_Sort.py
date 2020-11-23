def SelectionSort(A, size):
    for step in range(size):
        min_index = step

        for i in range(step+1, size):
            if A[i] < A[min_index]:
                min_index = i

        (A[step], A[min_index]) = (A[min_index], A[step])


if __name__ == '__main__':
    A = input().split()
    size = len(A)
    SelectionSort(A, size)
    print(A)
