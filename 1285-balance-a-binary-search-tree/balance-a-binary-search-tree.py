class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        #  perform in-order traversal and collect node values
        def in_order_traversal(node):
            if not node:
                return []
            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
        
        # construct a balanced BST from sorted node values
        def sorted_array_to_bst(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = sorted_array_to_bst(nums[:mid])
            node.right = sorted_array_to_bst(nums[mid+1:])
            return node
        
        # Get the sorted node values from the BST
        sorted_vals = in_order_traversal(root)
        
        # Construct and return a balanced BST
        return sorted_array_to_bst(sorted_vals)

