class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1]
        suffix = [1]

        for idx in range(len(nums)-1):
            prefix.append(nums[idx]*prefix[-1])
        
        for idx in range(len(nums)-1,0,-1):
            suffix.append(nums[idx] * suffix[-1])

        suffix = suffix[::-1]
        #print('suffix',suffix)
        #print('prefix',prefix)
        output = [suffix[idx]*prefix[idx] for idx in range(len(prefix))] 
        return output




