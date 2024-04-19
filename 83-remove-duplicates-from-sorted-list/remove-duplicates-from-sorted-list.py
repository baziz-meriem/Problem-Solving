# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.val = float('-inf')
        dummy_node.next = head
        prev = dummy_node
        current = head

        while current:
            if prev.val == current.val:
                prev.next = current.next
                
            else:
                prev = current
            current = current.next


        return dummy_node.next

