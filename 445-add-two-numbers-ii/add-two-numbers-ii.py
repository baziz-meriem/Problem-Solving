# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1_list = []
        num2_list = []
        node1 = l1
        node2=l2
        while node1 :
            num1_list.append(str(node1.val))
            node1 = node1.next

        while node2:
            num2_list.append(str(node2.val))
            node2 = node2.next

        nums = list(str(int(''.join(num1_list))+int(''.join(num2_list))))[::-1]
        prev = None
        for num in nums:
            new_node = ListNode()
            new_node.next = prev
            new_node.val = int(num)
            prev = new_node

        return new_node