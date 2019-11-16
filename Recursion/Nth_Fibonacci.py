# Nth fibonacci
# Time complexity without memoization converge to 2^n, because for each given n we call 2 function fib(n-1) and fib(n-2) and each function calls 2 fuctions and so on and so forth

cache = {}
def fib(self, n):
    if n in cache:
        return cache[n]
    else:
	if n == 0 : return 0
	if n == 1 or n == 2: return 1
	cache[n] = fib(n - 2) + fib(n - 1) 
	return 	cache[n] 
