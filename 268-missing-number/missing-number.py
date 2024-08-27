class Solution:
    def missingNumber(self,nums):
        n = len(nums)
        # XOR all numbers from 0 to n
        xor_range = 0
        for i in range(n + 1):
            xor_range ^= i
        
        # XOR all numbers in the array
        xor_array = 0
        for num in nums:
            xor_array ^= num
        
        # XOR the results of the above two steps to find the missing number
        missing = xor_range ^ xor_array
        return missing
