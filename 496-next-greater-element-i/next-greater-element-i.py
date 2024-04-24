from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_dict = defaultdict(int)
        stack = [nums2[0]]
        for num in nums2[1:]:
            if stack and num <= stack[-1]:
                nums_dict[stack[-1]] = -1

            while stack and num > stack[-1]:
                nums_dict[stack.pop()] = num



            stack.append(num)
        nums_dict[stack.pop()] = -1

        return [nums_dict[num] for num in nums1]