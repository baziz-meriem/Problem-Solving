from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_nums = []
        negative_nums = []
        
        for num in nums:
            if num > 0:
                positive_nums.append(num)
            else:
                negative_nums.append(num)

        modified_list = []
        pos = True
        while positive_nums or negative_nums:
            if pos:
                if positive_nums:
                    modified_list.append(positive_nums.pop(0))
                else:
                    modified_list.append(negative_nums.pop(0))
            else:
                if negative_nums:
                    modified_list.append(negative_nums.pop(0))
                else:
                    modified_list.append(positive_nums.pop(0))
            pos = not pos

        return modified_list
