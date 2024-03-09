class Solution:
    def maxArea(self, height: List[int]) -> int:
        start_idx = 0
        end_idx = len(height)-1
        max_content = 0

        while start_idx != end_idx:
            current_content =  min(height[start_idx],height[end_idx])*(end_idx-start_idx)
            if current_content > max_content:
                max_content = current_content
            if height[start_idx] > height[end_idx]:
                end_idx -= 1
            else:
                start_idx += 1

        return max_content
            