# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal=[]
        def inorder(node):
            if node is not None:
                
                inorder(node.left)
                self.traversal.append(node.val)
                inorder(node.right)
            return self.traversal
            
        
        return inorder(root)