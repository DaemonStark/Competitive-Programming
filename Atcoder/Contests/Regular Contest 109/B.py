def findMinimum(arr, n, k):

    res = 0
    i = 0
    while(n):

        # Buy current candy
        res += arr[i]

        # And take k
        # candies for free
        # from the last
        n = n-k
        i += 1
    return res


# Driver code
arr = [3, 2, 1, 4]
n = len(arr)
k = 2

arr.sort()

# Function call
print(findMinimum(arr, n, k))
