# Find closest value in BST

# Recursif approach: 
# Time complexity: 
#   -> Average case: O(log(n)), where n is the number of nodes (Beacause we are exploring either the right or the left side of the tree)
#   -> Worst case: O(n), where n is the number of nodes | when we only have one branch
# Space complexity: 
#   -> Average case: O(log(n)), where n is the number of nodes (Due to recursion on Python)
#   -> Worst case: O(n), where n is the number of nodes | when we only have one branch


def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    if not tree:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if tree.value > target:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif tree.value < target:
        return findClosestValueInBstHelper(tree.right, target, closest)
    elif tree.value == target:
        return tree.value
    
        

