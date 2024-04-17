# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_pointer = head
        slow_pointer = head
        
        while fast_pointer:
            if fast_pointer.next:
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
            else: 
                fast_pointer =None
            
        return slow_pointer
