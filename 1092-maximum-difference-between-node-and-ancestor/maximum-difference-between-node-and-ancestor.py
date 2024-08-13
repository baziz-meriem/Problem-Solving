from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def traverse(node, current_min, current_max):
            if not node:
                return current_max - current_min

            current_min = min(current_min, node.val)
            current_max = max(current_max, node.val)

            left_diff = traverse(node.left, current_min, current_max)
            right_diff = traverse(node.right, current_min, current_max)
            
            return max(left_diff, right_diff)
        
        
        return traverse(root, root.val, root.val)
