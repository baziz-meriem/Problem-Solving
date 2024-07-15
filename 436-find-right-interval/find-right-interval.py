class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        first = sorted([ [arr[0], i] for i,arr in enumerate(intervals) ]) + [[float('inf'), -1]]
        return [ first[ bisect_left(first, [arr[1]] )][1] for arr in intervals ]