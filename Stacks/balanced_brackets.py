# Balanced brackets 

def is_match(a, b):
	if a == "(" and b == ")" or a == "{" and b == "}" or a == "[" and b == "]":
		return True
	return False

def balancedBrackets(string):
	stack = []
	for c in string:
		if c == "(" or c == "{" or c == "[":
			stack.append(c)
		elif len(stack) != 0:
			if is_match(stack[-1], c):
				stack.pop()
			elif not is_match(stack[-1], c):
				return False
		elif len(stack) == 0:
			return False
	return len(stack) == 0
