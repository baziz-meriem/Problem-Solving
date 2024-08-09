# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def inorder(node):
            if node: 
                inorder(node.left)   
                nums.append(node.val)
                inorder(node.right)

        def construct(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = construct(left, mid - 1)
            node.right = construct(mid + 1, right)
            return node
        
        nums = []
        inorder(root)
        return construct(0, len(nums) - 1)