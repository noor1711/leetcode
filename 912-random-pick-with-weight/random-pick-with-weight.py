import random
class Solution:
    def __init__(self, w: List[int]):
        random.seed(10)
        # cumulative freq sum
        # 10**4 calls - we can do a binary search or a normal iteration over the weighted sum space
        weightedSum = []
        total = 0
        for weight in w:
            total += weight
            weightedSum.append(total)
        self.total = total
        self.weightedSum = weightedSum

    def pickIndex(self) -> int:
        randomNum = random.random() * self.total

        for index, weight in enumerate(self.weightedSum):
            if weight >= randomNum:
                return index

        return len(self.weightSum) - 1 # dead code


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()