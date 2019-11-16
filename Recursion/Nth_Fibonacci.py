# Nth fibonacci


cache = {}
def getNthFib(self, n):
    if n in cache:
        return cache[n]
    else:
	if n == 0 : return 0
	if n == 1 or n == 2: return 1
	cache[n] = getNthFib(n - 2) + getNthFib(n - 1) 
	return 	cache[n] 
