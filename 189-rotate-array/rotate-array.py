class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Ensure k is within the range of the list length
        
        nums[:] = nums[-k:] + nums[:-k]  # Rotate the list in place
