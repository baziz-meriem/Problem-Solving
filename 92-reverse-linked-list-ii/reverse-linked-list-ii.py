class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)  
        dummy.next = head
        prev = dummy

        # Move prev to the node just before the start of the reversal segment
        for _ in range(left - 1):
            prev = prev.next
        
        # Start reversal
        reverse = None
        curr = prev.next
        for _ in range(right - left + 1):
            next_temp = curr.next
            curr.next = reverse
            reverse = curr
            curr = next_temp

        # Connect the reversed part back to the list
        prev.next.next = curr
        prev.next = reverse

        return dummy.next
