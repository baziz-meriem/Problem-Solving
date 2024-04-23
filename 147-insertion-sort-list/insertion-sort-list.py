# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        dummy_node.val = float('-inf')

        prev= dummy_node
        curr = head
        while curr :
            if curr.val >= prev.val:
                curr = curr.next
                prev= prev.next
            else:
                start = dummy_node
                while start.next != curr:
                    prev.next = curr.next
                    if start.next.val > curr.val:
                        curr.next = start.next
                        start.next = curr
                        break
                    start = start.next

                curr = prev.next if prev else None

        return dummy_node.next