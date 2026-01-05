class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # nums are in the range - -10 to 10
        # length is 6
        # n! possibilities 
        # given the arr, insert the curr element at all possible points 
        n = len(nums)
        ans = []

        def recurse(index, arr):

            if index == n:
                ans.append(arr)
                return

            num = nums[index]

            for indi in range(len(arr) + 1):
                newArr = [*arr]
                newArr.insert(indi, num)
                recurse(index + 1, newArr)
            
        recurse(0, [])
        return ans