from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_idx = 0
        second_idx = 0
        intersect = []
        
        while first_idx < len(firstList) and second_idx < len(secondList):
            res = [max(firstList[first_idx][0], secondList[second_idx][0]), min(firstList[first_idx][1], secondList[second_idx][1])]
            if res[1] >= res[0]:
                intersect.append(res)

            next_start_first = firstList[first_idx][1] if first_idx < len(firstList) - 1 else float('inf')
            next_start_second = secondList[second_idx][1] if second_idx < len(secondList) - 1 else float('inf')

            if next_start_first < next_start_second:
                first_idx += 1
            else:
                second_idx += 1
                
        return intersect
