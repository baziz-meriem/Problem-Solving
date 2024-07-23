from collections import deque
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        min_queu = deque()
        max_queu = deque()
        numSub = 0
        l = 0
        for r,v in enumerate(nums):
            #update the queues
            while max_queu and max_queu[-1][1]<=v:
                max_queu.pop()
            max_queu.append([r,v])

            while min_queu and min_queu[-1][1]>=v:
                min_queu.pop()
            min_queu.append([r,v])
            
           
            #caculate the subarrays
            while max_queu[0][1] - min_queu[0][1] >2:
                if max_queu[0][0] == l:
                    max_queu.popleft()
                if min_queu[0][0] == l:
                    min_queu.popleft()
                l += 1 

            numSub += r-l+1
        return numSub