
def maxSubArray(A):
    maxSum = A[0]
    n = len(A)
    currMax = A[0]

    for i in range(1, n):
        currMax = max(A[i], currMax + A[i])
        maxSum = max(currMax, maxSum)
    return maxSum

print(maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3]))