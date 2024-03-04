class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted([x for x,y in points])
        max_width=0
        for idx in range(len(points)-1):
            difference = points[idx+1] - points[idx]
            if difference > max_width:
                max_width = difference
        return max_width
        