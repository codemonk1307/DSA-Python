

# Problem Statement -> https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

#Function to return max value that can be put in knapsack of capacity W.
def knapSack(self, W, wt, val, n):
    
    t = [[0]*(W+1) for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(W+1):
            
            if i == 0 or j == 0:
                t[i][j] = 0
            elif wt[i-1] <= j:
                t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
                
    return t[n][W]


# Note ->

# given weights and values of N items
# wt - weight array weights of each item
# val - value array cost of each item 
# W - capacity of Knapsack 
# t - 2-d array for storing values top-down DP approach