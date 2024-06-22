# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # define a function to traverse the tree and find the lowest common ancestor of two nodes
        def traverse(root, p, q):
            # base case: return None when the node is None
            if not root:
                return None
            # return the node itself when it's one of the target nodes
            if root == p or root == q:
                return root
            # recursively search the left and right subtrees
            left = traverse(root.left, p, q)
            right = traverse(root.right, p, q)
            # if both left and right subtrees return a valid node, the current node is the lowest common ancestor
            if left and right:
                return root
            # if only one subtree returns a valid node, return that node
            return left or right

        # call the traverse function to find the lowest common ancestor
        return traverse(root, p, q)


        # Find the lowest common ancestor
        lowest_common_ancestor = None
        for node in common_ancestors:
            if lowest_common_ancestor is None or node.val < lowest_common_ancestor.val:
                lowest_common_ancestor = node

        return lowest_common_ancestor