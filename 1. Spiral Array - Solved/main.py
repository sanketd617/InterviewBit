
def spiralOrder(A):
    k = 0
    l = 0
    m = len(A)
    n = len(A[0])
    result = []

    while (k < m and l < n):
        for i in range(l, n):
            result += [A[k][i]]

        k += 1

        for i in range(k, m):
            result += [A[i][n - 1]]

        n -= 1

        if (k < m):

            for i in range(n - 1, (l - 1), -1):
                result += [A[m - 1][i]]

            m -= 1

        if (l < n):
            for i in range(m - 1, k - 1, -1):
                result += [A[i][l]]

            l += 1

    return result


# A = [[0, 1, 2, 3],
#      [15, 16, 17, 4],
#      [14, 23, 18, 5],
#      [13, 22, 19, 6],
#      [12, 21, 20, 7],
#      [11, 10, 9, 8]]

# A = [[0]]

# A = [[1], [2]]

A = [
[0, 1, 2],
  [9, 10, 3],
  [8, 11, 4],
  [7, 6, 5]
]

# A = [
# [0, 1, 2, 3, 4],
#   [13, 14, 15, 16, 5],
#   [12, 19, 18, 17, 6],
# ]

print(spiralOrder(A))