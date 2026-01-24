class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxSum = nums[0] + nums[-1]

        for i in range(len(nums)//2):
            maxSum = max(maxSum, nums[i] + nums[-(i + 1)])
        
        return maxSum