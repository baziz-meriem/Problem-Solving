# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = []

        def helper(root , path):
            if not root:
                return
            path += str(root.val)
            if not(root.left or root.right):
                paths.append(path)
                return
            helper(root.left, path)
            helper(root.right, path)
        helper(root , "")
        total = 0
        for p in paths:
            total += int(p)
        return total