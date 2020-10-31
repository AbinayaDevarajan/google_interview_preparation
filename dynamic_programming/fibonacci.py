
import timeit

"""
Top down approach by using the recursion:
"""
def fibonacci(input):
    if input ==0: 
        return 1 
    elif input ==1:
        return 1 
    else:
        return fibonacci(input-1) + fibonacci(input -2 )


"""
memoization usage of cache
"""
def fibonacci_memo(input, cache=None):
    if input ==0: 
        return 1 
    if input ==1:
        return 1 
    if cache is None: cache ={}
    if input in cache: return cache[input]
    result = fibonacci_memo(input-1,cache) + fibonacci_memo(input-2,cache)
    cache[input] = result 
    print(cache) # this cache grows at each level and the recursive computations are avoided if it is already in cache
    return result



"""
Bottom up by using the tabulation method 
"""

def fibonacci_tablulation(n):
  dp = [0, 1]
  for i in range(2, n + 1):
    dp.append(dp[i - 1] + dp[i - 2])
  return dp[n]
    



print(fibonacci_memo(10))
print(fibonacci_tablulation(10))