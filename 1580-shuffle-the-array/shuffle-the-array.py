class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        idx1=0
        out=[] 
        for idx,i in enumerate(nums):
            
            if idx%2 ==0:
                out.append(nums[idx1]) 
                
            else : 
                out.append(nums[idx1+n])
                idx1 +=1
        return out
                