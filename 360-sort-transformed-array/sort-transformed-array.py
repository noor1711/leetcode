
class Solution:

    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        # okay so we are apply a quadratic function - U shape 
        # instead of sorting again, we can do a two point approach 
        start = 0
        end = len(nums) - 1

        def getQuadratic(x):
            return a * pow(x, 2) + b * x + c
        mappedArr = list(map(getQuadratic, nums))

        # now we need to just merge the two tails of the parabola
        ans = []
        while start <= end:
            qStart = mappedArr[start]
            qEnd = mappedArr[end]

            if a <= 0: # ends will be min, and center will be max
                if qStart <= qEnd:
                    ans.append(qStart)
                    start += 1
                else:
                    ans.append(qEnd)
                    end -= 1
                continue

            if qStart >= qEnd:
                ans.append(qStart)
                start += 1
            else:
                ans.append(qEnd)
                end -= 1
        
        return  ans if a <= 0 else ans[::-1]
