class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # we have index1 and index 2, either we can skip 1 or skip 2 or multiply 1 and 2    
        n = len(nums1)
        m = len(nums2)

        @lru_cache(None)
        def recurse(index1, index2):
            if index1 == n or index2 == m:
                return - 10 ** 9

            num1 = nums1[index1]
            num2 = nums2[index2]

            one = recurse(index1 + 1, index2)
            two = max(0, recurse(index1 + 1, index2 + 1)) + num1 * num2
            three = recurse(index1, index2 + 1)

            return max(one, two, three)
        
        return recurse(0, 0)
