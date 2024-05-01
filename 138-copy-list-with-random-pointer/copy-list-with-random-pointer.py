"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # First pass: Make copy of each node,
        # and link them together side-by-side in a single list.
        current = head
        while current:
            new_node = Node(current.val, current.next)
            current.next = new_node
            current = new_node.next

        # Second pass: Assign random pointers for the copy nodes.
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Third pass: Restore the original list, and separate the copy list.
        current = head
        pseudo_head = Node(0)
        copy_current = pseudo_head
        while current:
            next_original = current.next.next  # Save the next element
            copy_current.next = current.next
            copy_current = copy_current.next
            current.next = next_original  # Restore the original list
            current = next_original

        return pseudo_head.next
            