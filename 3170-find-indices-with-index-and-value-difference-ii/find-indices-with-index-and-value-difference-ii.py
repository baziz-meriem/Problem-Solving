from sortedcontainers import SortedList

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        S = SortedList()

        for i in range(n):
            if i >= indexDifference:
                x = i - indexDifference
                y = nums[x]
                S.add((y, x))

            upper_bound = S.bisect_left((nums[i] + valueDifference, 0))
            if upper_bound != len(S):
                return [S[upper_bound][1], i]

            lower_bound = S.bisect_left((nums[i] - valueDifference + 1, 0))
            if lower_bound > 0:
                return [S[lower_bound - 1][1], i]

        return [-1, -1]
