class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums,reverse=True)
        nums_dict={}
        for idx,num in enumerate(nums_sorted):
            if num not in nums_dict.keys():
                nums_dict[num]=idx
                
        operations=0
        set_nums = set(nums_sorted)

        for num in set_nums :
                operations += nums_dict[num]
        return operations
            
        