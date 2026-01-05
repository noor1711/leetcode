class Solution:
    def isPalindromic(self, s):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        # 15 slots - sticks - 0 - 15,  15C0  + 15C1 + 15C2 .... 15C15  = 2 ^ 15 possibilities 
        ans = []
        n = len(s)

        def recurse(index, arr):
            if index == n:
                ans.append(arr)
                return 

            for end in range(index + 1, n + 1):
                curr = s[index:end]
                if self.isPalindromic(curr):
                    recurse(end, [*arr, curr])

        recurse(0, [])
        return ans