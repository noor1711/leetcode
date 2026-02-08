# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root):
        if root is None:
            return True, 0
        
        isValidLeft, left = self.getHeight(root.left)
        if not isValidLeft:
            return False, left + 1

        isValidRight, right = self.getHeight(root.right)
        if not isValidRight:
            return False, right + 1

        return abs(right - left) <= 1, max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.getHeight(root)[0]