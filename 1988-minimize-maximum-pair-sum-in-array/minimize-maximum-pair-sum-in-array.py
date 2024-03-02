from collections import deque
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums_q= deque(sorted(nums)) 

        tuple_list=[]
        while nums_q:
            tup1 = nums_q.popleft()
            tup2 = nums_q.pop()
            tuple_list.append((tup1,tup2))
        max_tup = max(list(tup1+tup2 for tup1,tup2 in tuple_list))
        return max_tup

