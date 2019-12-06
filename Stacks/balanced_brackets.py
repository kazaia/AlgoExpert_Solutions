# Balanced brackets 
# Time complexity: O(n)
# Space complexity: O(n)

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



# Solution 2:
# Time complexity: O(n)
# Space complexity: O(n)

def balancedBrackets(string):
    openingBrackets = "{(["
    closingBrackets =  "}])"
    matchingBrackets = {"}":"{", ")":"(", "]":"["}
    stack = []
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == matchingBrackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0       
