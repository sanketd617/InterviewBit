
def plusOne(A):
    n = len(A)
    x = 0

    if n == 1 and A[0] == 0:
        return [1]

    while A[x] == 0:
        x += 1

    A = A[x:]
    n = n - x
    c = 1

    i = n-1

    while True:
        if i < 0:
            A = [0] + A
            i = 0
        a = A[i]
        a += c
        if a > 9:
            A[i] = 0
            i -= 1
            continue
        A[i] = a
        break

    return A

print(plusOne([0]))