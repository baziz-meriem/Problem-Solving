# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 , p2 = l1, l2
        num1=[]
        num2=[]
        while p1 or p2:
            if p1:
                num1.append(str(p1.val))
                p1 = p1.next
            if p2:
                num2.append(str(p2.val))
                p2 = p2.next

        
        result = list(str(int(''.join(num1)[::-1])+int(''.join(num2)[::-1])))
        
        new_list = ListNode()
        prev = None
        for num in result:
            new_node =  ListNode()
            new_node.val = int(num)
            new_node.next = prev
            prev = new_node
            
            

        return new_node