class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for index, num in enumerate(nums):
            newIndex = (index + num) % n
            result[index] = nums[newIndex]

        return result