class Solution:
    def calcOps(self, s, curr):
        ans = 0
        for l in s:
            if int(l) != curr:
                ans += 1
            curr = 1 - curr
        return ans

    def minOperations(self, s: str) -> int:
        # the string either starts with 0 or with 1 
        withOne = 0 
        return min(self.calcOps(s, 1), self.calcOps(s, 0))
        
