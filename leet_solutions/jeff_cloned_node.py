# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# Initially had trouble with this one because I didn't store the left and right
# node searches to check for None before returning. As a result, the function kept
# returning none/null.


def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    if original == None or original == target:
        return cloned
    else:
        left = getTargetCopy(original.left, cloned.left, target)
        if left:
            print("In original left call")
            return left
        right = getTargetCopy(original.right, cloned.right, target)
        if right:
            print("In original right call")
            return right
