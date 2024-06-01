


# Problem Statement -> https://leetcode.com/problems/partition-equal-subset-sum/

def canPartition(self, nums: list[int]) -> bool:
        
    n, sumNums = len(nums), sum(nums)
    halfSum = sumNums // 2
    
    if n == 1 or not nums: return False
    # sum of array is odd -> can't be partitioned in two parts of equal sum
    if sumNums % 2: return False
    
    # 2-D arrays -> [[val] * columns] * rows
    dp = [[False]* (halfSum + 1) for i in range(n + 1)]

    # Base Condition - Initialization            
    for i in range(n + 1):
        for j in range(halfSum + 1):
            if i == 0: 
                dp[i][j] = False  
            if j == 0: 
                dp[i][j] = True

    # Choices Diagram Code             
    for i in range(1,n + 1):
        for j in range(1,halfSum + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]    
            else:
                dp[i][j] = dp[i - 1][j]
                            
    return dp[n][halfSum]