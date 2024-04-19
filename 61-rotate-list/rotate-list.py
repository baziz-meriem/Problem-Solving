# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        node = head
        total = 0
        if head and head.next :
            while node:
                node = node.next
                total += 1
                
            if not k % total:
                return dummy_node.next

            stop_idx = total - k % total

            node = head
            cpt = 1
            start_p = head
            while node.next:
                if cpt == stop_idx:
                    start_p = node
                    
                node = node.next
                cpt += 1
        
            dummy_node.next = start_p.next
            start_p.next = None
            node.next = head
        return dummy_node.next