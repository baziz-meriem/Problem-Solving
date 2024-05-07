from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = deque()  
        min_queue = deque()  

        left = 0

        for n in nums:
            
            while max_queue and n > max_queue[-1]:
                max_queue.pop()
            max_queue.append(n)

            
            while min_queue and n < min_queue[-1]:
                min_queue.pop()
            min_queue.append(n)

            if max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[left]:
                    max_queue.popleft()
                if min_queue[0] == nums[left]:
                    min_queue.popleft()
                left += 1

        return len(nums) - left