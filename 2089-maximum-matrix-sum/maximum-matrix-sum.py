class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        rows = []
        minPoss = 10 ** 9
        neg = 0
        zero = 0
        total = 0
        for row in matrix:
            negs = 0
            zeros = 0
            for val in row:
                if val < 0:
                    negs += 1
                elif val == 0:
                    zeros += 1
                minPoss = min(minPoss, abs(val))
                total += abs(val)

            zero += zeros
            if negs % 2:
                if not zeros:
                    neg += 1

        if neg % 2:
            total -= 2 * minPoss

        return total