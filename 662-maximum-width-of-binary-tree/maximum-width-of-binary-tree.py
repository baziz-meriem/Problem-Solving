# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(Node,depth,position):
            if not Node:
                return
            if depth not in leftmost_dict:
                leftmost_dict[depth] = position
            current_width = position - leftmost_dict[depth] + 1
            nonlocal max_width
            max_width = max(max_width,current_width)
            dfs(Node.left,depth+1,position*2)
            dfs(Node.right,depth+1,position*2+1)
        leftmost_dict = {}
        max_width=0
        dfs(root,0,0)
        return max_width