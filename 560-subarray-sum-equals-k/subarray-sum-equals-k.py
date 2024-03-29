class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = [nums[0]]
        count = 0
        for idx in range(1,len(nums)):
            pref.append(nums[idx] + pref[-1])
        
        count_dict = {0:1}
        for num in pref:
            target = num - k
            if target in count_dict:

                count += count_dict[target]
            if num not in count_dict:
                count_dict [num] = 1
            else:
                count_dict[num] += 1

        return count