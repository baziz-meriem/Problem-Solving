class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current=1
        idx=0
        size=len(nums)


        while idx<len(nums)-1:
            
            if nums[idx]==nums[idx+1]:
                current += 1
                    
                if current >2:
                    del nums[idx]
                    current -= 1
                    size -= 1
                else:
                    idx += 1
            else:
                current =1
                idx += 1


        return size
