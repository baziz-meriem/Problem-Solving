class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:      
        queue_max, queue_min = deque(), deque()
        left, prev_max, prev_min, ans = 0, 0, 0, 0
        for i, num in enumerate(nums):
            while queue_max and nums[queue_max[0]] - num > 2:
                prev_max = queue_max.popleft()
            while queue_max and num > nums[queue_max[-1]]:
                queue_max.pop()
            queue_max.append(i)

            while queue_min and num - nums[queue_min[0]] > 2:
                prev_min = queue_min.popleft()    
            while queue_min and num < nums[queue_min[-1]]:
                queue_min.pop()
            queue_min.append(i)
        
            if nums[prev_max] - num > 2:
                left = queue_max[0]
            elif num - nums[prev_min] > 2:
                left = queue_min[0]
            ans += i - left + 1      
        return ans