
def coverPoints(A, B):
    n = len(A)
    result = 0
    for i in range(1, n):
        x = A[i-1]
        y = B[i-1]
        nx = A[i]
        ny = B[i]
        ans = 0
        dx = abs(nx - x) + 1
        dy = abs(ny - y) + 1

        if dx > dy:
            ans += dy - 1
            ans += dx - dy
        else:
            ans += dx - 1
            ans += dy - dx

        # print(ans)

        result += ans
    return result


print(coverPoints([0, 1, 2, 0, 0], [0, 1, 2, 2, 0]))