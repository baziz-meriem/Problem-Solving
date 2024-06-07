class Solution:
    def subsets(self, nums):
        def backtrack(start, path):
            results.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i]) 
                backtrack(i + 1, path)
                path.pop()
        
        results = []
        backtrack(0, [])
        return results