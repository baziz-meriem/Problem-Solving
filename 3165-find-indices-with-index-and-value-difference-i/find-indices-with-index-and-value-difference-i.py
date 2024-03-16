class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
            def valueDiff(i,j,target=valueDifference):
                if abs(nums[i] - nums[j]) >= target:
                    return True
                else:
                    return False
        
            def indexDiff(i,j,target=indexDifference):
                if abs(i - j) >= target:
                    return True
                else:
                    return False
            
            for idx in range(len(nums)):
                r_idx = len(nums)-1
               
                while r_idx >= idx:
                    if not indexDiff(r_idx,idx):
                       
                        if r_idx== len(nums)-1 and idx==0:
                            return [-1,-1]
                        else:
                            break
                    else:
                        
                        if valueDiff(r_idx,idx):
                            return [r_idx,idx]
                        else:
                            r_idx -= 1
            return [-1,-1]
           
                