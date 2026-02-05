class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for index, num in enumerate(nums):
            if num > 0:
                right = num
                newIndex = (index + right) % n
                result[index] = nums[newIndex]
            elif num < 0:
                left = abs(num)
                newIndex = (index - left) % n
                result[index] = nums[newIndex]
            else:
                result[index] = num

        return result