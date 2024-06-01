

# Problem Statement -> https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1/#


def isSubsetSum (self, n, arr, sum):
        
    t = [[0]*(sum+1) for _ in range(n+1)]
    
    # Base Condition - Initilization
    for i in range(n+1):
        for j in range(sum+1):
            if i == 0:
                t[i][j] = False
            if j == 0:
                t[i][j] = True

    # Code for choices             
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j] or t[i-1][j-arr[i-1]]
            else:
                t[i][j] = t[i-1][j]
                
    return t[n][sum]


# Note ->

# given array of non-negative integers, and a value sum
# arr - array of non negative numbers
# sum - sum to be obtained from subset of array
# t - 2-d array for storing values top-down DP approach