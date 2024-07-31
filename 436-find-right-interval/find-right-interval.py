from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        sorted_intervals = sorted((interval[0], idx) for idx, interval in enumerate(intervals))
        res = [-1] * len(intervals)
        

        def binary_search(target):
            low, high = 0, len(sorted_intervals)
            while low < high:
                mid = (low + high) // 2
                if sorted_intervals[mid][0] >= target:
                    high = mid
                else:
                    low = mid + 1
            return low
        
        # For each interval, find the right interval using binary search
        for idx, (start, end) in enumerate(intervals):

            pos = binary_search(end)
            if pos < len(sorted_intervals):
                res[idx] = sorted_intervals[pos][1]
        
        return res
