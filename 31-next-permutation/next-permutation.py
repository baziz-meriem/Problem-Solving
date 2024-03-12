class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
    
        """
        available_nums = []
        #keep an ordered list of  the inserted elements starting from the end
        available_nums.append(nums[-1])
        

        idx = len(nums)-2
        #move to the left of the list
        while idx >= 0:
            if nums[idx] >= available_nums[-1]:
                available_nums.append(nums[idx])
                available_nums.sort()
                idx -= 1
            else:
                for i,n in enumerate(available_nums):
                    if n > nums[idx]:
                        nums[idx], available_nums[i] = available_nums[i],nums[idx]
                        available_nums.sort()
                        nums[idx+1:]  = available_nums[:]

                        return nums
                
                break


        if idx<0:
            nums.sort()
        return nums
        

