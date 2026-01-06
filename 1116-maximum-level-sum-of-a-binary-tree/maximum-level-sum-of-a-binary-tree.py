# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # bfs
        cue = deque()
        cue.append([root, 1])
        maxSum = root.val
        prevLev = 0
        currSum = root.val
        ans = 1

        while cue:
            curr, lev = cue.popleft()

            if lev != prevLev:
                if currSum > maxSum:
                    maxSum = currSum
                    ans = prevLev
                prevLev = lev
                currSum = 0

            currSum += curr.val
            if curr.left:
                cue.append([curr.left, lev + 1])
            if curr.right:
                cue.append([curr.right, lev + 1])
        else:
            if currSum > maxSum:
                ans = lev

        return ans