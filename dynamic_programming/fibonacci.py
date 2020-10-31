
import timeit
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

print(fibonacci_memo(10))
