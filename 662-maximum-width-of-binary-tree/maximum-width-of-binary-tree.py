class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node, depth, position):
            if not node:
                return
            
            if depth not in leftmost_positions:
                leftmost_positions[depth] = position
            
            current_width = position - leftmost_positions[depth] + 1
            nonlocal max_width
            max_width = max(max_width, current_width)
            
            dfs(node.left, depth + 1, 2 * position)
            dfs(node.right, depth + 1, 2 * position + 1)

        leftmost_positions = {}
        max_width = 0
        dfs(root, 0, 0)
        return max_width
