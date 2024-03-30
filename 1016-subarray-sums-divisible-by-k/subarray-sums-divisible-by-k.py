class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        tot_subarrays = 0
        nums_dict = {0: 1}  # Starting with 0:1 accounts for subarrays starting from the beginning.
        running_sum_mod_k = 0
        
        for num in nums:
            running_sum_mod_k = (running_sum_mod_k + num) % k
            if running_sum_mod_k in nums_dict:
                tot_subarrays += nums_dict[running_sum_mod_k]
            
            if running_sum_mod_k not in nums_dict:
                nums_dict[running_sum_mod_k] = 1
            else:
                nums_dict[running_sum_mod_k] += 1
        
        return tot_subarrays
