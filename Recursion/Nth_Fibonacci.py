# Nth fibonacci
# Time complexity without memoization converge to 2^n:
# For each given n we call 2 function fib(n-1) and fib(n-2) and each function calls 2 fuctions and so on and so forth

# Space complexity: O(n) beacause of the function callstack 

# Time complexity with memoization:
# Because we are calculating every fib(n) just once
# Space complexity: O(n) because of the recursive call stack and also because of the created dictionary with the lenght of n elements. 

cache = {0:0, 1:1, 2:1}
class Solution:
    def fib(self, n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = self.fib(n - 2) + self.fib(n - 1) 
            return 	cache[n] 


