# Branch sums: 

# Time complexity: O(n)
# Space complexity: O(n)



# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sums = []
    computeBranchSums(root, 0, sums)
    return sums

def computeBranchSums(root, runningSum, sums):
    if not root:
        return []
    newRunningSum = runningSum + root.value
    if not root.left and not root.right:
        sums.append(newRunningSum)
        return
    computeBranchSums(root.left, newRunningSum, sums)
    computeBranchSums(root.right, newRunningSum, sums)
