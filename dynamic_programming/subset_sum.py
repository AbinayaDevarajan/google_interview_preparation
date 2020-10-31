"""
Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}

Input: {1, 2, 7, 1, 5}, S=10
Output: True
The given set has a subset whose sum is '10': {1, 2, 7}

Input: {1, 3, 4, 8}, S=6
Output: False
The given set does not have any subset whose sum is equal to '6'.

"""

"""
Bottom up dynamic programming approach
"""

def solve_subset_sum(num=[],sum = None):
     
    n = len(num)
    dp = [[False for x in range(0,sum+1)] for y in range (0,n)]

    for x in range(0,n):
        dp[x][0] = True 
    
    for y in range(0,sum+1):
        dp[0][y] = True if y ==num[0] else False 

    
    for i in range(1,n):
        for s in range(1,sum+1):
            if dp[i][s-1]:
                dp[i][s] = dp[i-1][s]
            elif s >=num[i]:
                dp[i][s] = dp[i-1][s-num[i]]
    return dp[n-1][sum]

print(solve_subset_sum(num=[1,2,3,4,5], sum =10))
print(solve_subset_sum(num=[1,2,3,4,5], sum =19))
            