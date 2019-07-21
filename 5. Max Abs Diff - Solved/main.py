
def maxArr(A):
    a = []
    b = []
    minA = A[0]
    minB = A[0]
    maxA = A[0]
    maxB = A[0]
    n = len(A)
    for i in range(n):
        x = A[i] - i
        y = A[i] + i
        a += [x]
        b += [y]

        if minA > x:
            minA = x
        if minB > y:
            minB = y
        if maxA < x:
            maxA = x
        if maxB < y:
            maxB = y

    return max(maxA - minA, maxB - minB)

print(maxArr([1, 3, -1]))