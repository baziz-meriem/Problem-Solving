class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: 
        max_ones=0
        current_ones =0
        if 1 in nums:
             for num in nums:#[1,1,0,1,1,1]
                if num==1 :
                    current_ones +=1 #2
                else :
                    if  current_ones > max_ones:#true
                        max_ones = current_ones #max=2
                    current_ones =0
                if  current_ones > max_ones:#true
                    max_ones = current_ones #max=2
                
        return max_ones
        