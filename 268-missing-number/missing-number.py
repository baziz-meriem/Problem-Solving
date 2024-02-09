class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = 0
        nums = sorted(nums)
        length = len(nums)

        while num < length:
            if nums[num] == num :
                num += 1
            else :
                break;
        
        return num
        