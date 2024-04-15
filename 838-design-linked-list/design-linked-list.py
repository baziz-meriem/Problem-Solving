class Node:
    def __init__(self,value):
        self.next = None
        self.value = value

class MyLinkedList:

    def __init__(self):
       self.head = None
       self.cpt = 0


    def get(self, index: int) -> int:
        if self.cpt <= index or self.head is None:
            return -1
        else:        
            idx=0
            node = self.head
            while idx<index:
                idx += 1
                node = node.next
            return node.value
                

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.cpt += 1
        node = self.head


    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        node = self.head
        if node is None:
            self.head = new_node
        else:
            while node.next:
                node = node.next

            node.next = new_node
        self.cpt += 1
            

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.cpt :
            return 
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.cpt:
            self.addAtTail(val)
            return

        new_node = Node(val)
        idx = 0
        node = self.head
        while idx < index - 1:
            node = node.next
            idx += 1
        new_node.next = node.next
        node.next = new_node
        self.cpt += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.cpt:
            return
        if index == 0:
            self.cpt -= 1
            temp = self.head
            self.head = self.head.next
            del temp
            return
        else:
            idx = 0
            node = self.head
            while idx < index - 1:
                node = node.next
                idx += 1
            node.next = node.next.next
        self.cpt -= 1
                

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)