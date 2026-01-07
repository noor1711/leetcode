# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # find total sum, all nodes are positive yayy 
        # keep a list of sum at all diff nodes
        # product will be max at num nearest to sum // 2
        sums = []

        def recurse(root):
            if not root:
                return 0
            
            left = recurse(root.left)
            right = recurse(root.right)

            val = root.val
            sums.append(left + val + right)
            return left + val + right
        
        total = recurse(root)
        # find num nearest to total // 2
        curr = 0

        for num in sums:
            if abs(total / 2 - num) < abs(total / 2 - curr):
                curr = num

        # print(sums, curr)
        return (curr * (total - curr)) % (10 ** 9 + 7)
