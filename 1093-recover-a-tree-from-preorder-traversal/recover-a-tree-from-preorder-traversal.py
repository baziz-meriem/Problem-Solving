class Solution:
    def recoverFromPreorder(self, traversal):
        i, n = 0, len(traversal)
        # define a stack
        stack = []
        num = ''

        # iterate over traversal and parse tokens
        while i < n:
            # define a depth
            level = 0

            # to calculate it for a particular (next) node
            while i < n and traversal[i] == '-': 
                i += 1
                level += 1
            
            # but if a level is different one, pop redundant
            # elements from stack
            while stack and len(stack) > level: stack.pop()

            # then we should parse an integer, since it could have
            # more than 1 digit
            while i < n and traversal[i] != '-':
                num += traversal[i]
                i += 1

            # create a Binary Tree node
            node = TreeNode(int(num))

            # and fill it with children (for left)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            # for right node
            elif stack:
                stack[-1].right = node
                
            # don't forget to push a current node into stack
            stack.append(node)
            # and reset a previous integer
            num = ''
                
        # the first element of a stack is a root of a recovered tree
        return stack[0]