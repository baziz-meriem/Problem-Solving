from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack_deque = deque()
        node = head
        while node:
            stack_deque.append(node.val)
            node = node.next
        node = head
        while node:
            node.val = stack_deque.pop()
            node = node.next
        
        return head
