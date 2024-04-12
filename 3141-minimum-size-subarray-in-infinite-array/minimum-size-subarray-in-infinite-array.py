class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)
        copy = target // total
        target %= total  # Use target itself as the remaining part after full cycles

        # If after removing full cycles of sum(nums) there is nothing left to find, adjust answer
        if target == 0:
            return copy * n if copy > 0 else -1

        wind_sum = 0  # Start with no sum, checking for target in the remaining part
        min_wind = float('inf')
        s_wind, e_wind = 0, 0

        # Only need to consider target within 2*n to allow for wrapping
        while e_wind < 2 * n:
            wind_sum += nums[e_wind % n]

            while wind_sum >= target and s_wind <= e_wind:
                if wind_sum == target:
                    min_wind = min(min_wind, e_wind - s_wind + 1)
                wind_sum -= nums[s_wind % n]
                s_wind += 1

            e_wind += 1

        # Adjust the result for the cycles skipped
        return (min_wind + copy * n) if min_wind != float('inf') else -1