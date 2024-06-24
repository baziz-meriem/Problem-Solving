# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum =0
        def dfs(root, pV, gpV):
            nonlocal sum
            if root == None:
                return
            if gpV%2==0:
                sum+=root.val
            dfs(root.left, root.val, pV)
            dfs(root.right, root.val, pV)
        dfs(root.left, root.val, 1)
        dfs(root.right, root.val, 1)
        return sum