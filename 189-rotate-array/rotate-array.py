class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev_l = len(nums)
        k = k % prev_l
        nums.extend(nums[:-k])

        print(nums)
        l = len(nums) - prev_l
        del nums[:l]