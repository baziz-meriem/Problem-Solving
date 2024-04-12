class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)
        copy = target // total
        target %= total 

        
        if target == 0:
            return copy * n if copy > 0 else -1

        wind_sum = 0 
        min_wind = float('inf')
        s_wind, e_wind = 0, 0

        while e_wind < 2 * n:
            wind_sum += nums[e_wind % n]

            while wind_sum >= target and s_wind <= e_wind:
                if wind_sum == target:
                    min_wind = min(min_wind, e_wind - s_wind + 1)
                wind_sum -= nums[s_wind % n]
                s_wind += 1

            e_wind += 1

        
        return (min_wind + copy * n) if min_wind != float('inf') else -1