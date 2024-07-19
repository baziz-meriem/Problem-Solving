# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = []
        unvisited = deque([root] if root else [])

        while unvisited:
            for i in range(len(unvisited)):
                node = unvisited.popleft()
                level.append(node.val)

                if node.left:
                    unvisited.append(node.left)

                if node.right:
                    unvisited.append(node.right)

            res.append(level[::-1] if  len(res)%2 else level)
            level = []
        return res


