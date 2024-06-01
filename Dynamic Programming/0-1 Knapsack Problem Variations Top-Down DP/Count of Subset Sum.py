

# Problem Statement -> https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1#


def perfectSum(self, arr, n, sum):
		
    t = [[0]*(sum+1) for _ in range(n+1)]
    mod = 10 ** 9 + 7     # for very large input values

    # Base Condition - Initialization
    for i in range(n+1):
        for j in range(sum+1):
            if i == 0:
                t[i][j] = 0
            if j == 0:
                t[i][j] = 1

    # Choices             
    for i in range(1, n+1):
        for j in range(sum+1):
            if arr[i-1] <= j:
                t[i][j] = (t[i-1][j-arr[i-1]] + t[i-1][j]) % mod
            else:
                t[i][j] = (t[i-1][j]) % mod
                
    return t[n][sum] % mod