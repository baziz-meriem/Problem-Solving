# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        cpt=0
        while cpt < n and fast:
            
            fast = fast.next
            cpt += 1

        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next

        
        if slow.next:
            temp_slow=slow.next
            slow.next = slow.next.next if slow.next else None
            del temp_slow

            return head 
        else:
            return None
        
