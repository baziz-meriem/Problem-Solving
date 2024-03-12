class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        idx = 0

        while idx<=len(nums)-2:
            if nums[idx]==nums[idx+1]:
                print(nums[idx])
                return nums[idx]
            idx += 1
       