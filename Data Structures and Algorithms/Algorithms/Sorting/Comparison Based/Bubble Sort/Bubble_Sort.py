def BubbleSort(A):
    swapped = 1
    for i in range(len(A)):
        if(swapped == 0):
            return
        for k in range(len(A)-1, i, -1):
            if(A[k] < A[k-1]):
                A[k], A[k-1] = A[k-1], A[k]
                swapped = 1


if __name__ == "__main__":
    A = [112, 548, 758, 421, 689, 321]
    BubbleSort(A)
    print(A)
