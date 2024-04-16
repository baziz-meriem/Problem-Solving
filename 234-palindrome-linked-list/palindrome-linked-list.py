# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        my_pal =[]
        node = head
        while node:
            my_pal.append(str(node.val))
            node = node.next
        return ''.join(my_pal) == ''.join(my_pal[::-1])