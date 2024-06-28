# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        targetPath=""
        nodePaths=[]
        q=deque([(root, "")])

        # Build Path for each node from root using Level order traversal
        while(q):

            node, path=q.popleft()

            # Store the target path
            if node==target:
                targetPath=path

            nodePaths.append((node.val, path))

            # For left child add "l" in the path
            if node.left:
                q.append((node.left, path+"l"))
            # For right child add "r" in the path
            if node.right:
                q.append((node.right, path+"r"))

        # Find the length of path from root to target
        tpLen=len(targetPath)
        result=[]

        # For each node path
        for node, path in nodePaths:

            p=0
            tp=0
            pLen=len(path)
            
            # Cover the path that is common between current node
            # and the target node using two pointer
            while(p<pLen and tp<tpLen):
                
                # Break when the path is no longer common
                if path[p]!=targetPath[tp]:
                    break

                p+=1
                tp+=1

            # Distance= nodePath-commonPath + targetPath-commonPath
            dist=pLen-p+tpLen-tp
            if dist==k:
                result.append(node)

        return result

                    

        