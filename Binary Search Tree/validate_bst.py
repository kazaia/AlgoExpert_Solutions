# Validate BST 


# Time complexity: O(n) where n is the number of nodes 
# Space complexity: ?? 


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
	return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, minVal, maxVal):
	if not tree:
		return True 
	if tree.value < minVal or tree.value >= maxVal:
		return False
	leftIsValid = validateBstHelper(tree.left, minVal, tree.value)
	rightIsValid = validateBstHelper(tree.right, tree.value, maxVal)
	return leftIsValid and rightIsValid
