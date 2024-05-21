class MyCircularDeque:

    def __init__(self, k: int):
         self.k = k
         self.size = 0
         self.deque = [0] * k
         self.front =0
         self.rear=0



    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.front = (self.front - 1 + self.k)%self.k
            self.deque[self.front] = value
            self.size += 1
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.deque[self.rear] = value
            self.rear = (self.rear+1)%self.k
            self.size += 1

            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.k
            self.size -= 1
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.rear  = (self.rear - 1 + self.k) % self.k
            self.size -= 1
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.front]


    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.deque[(self.rear - 1 + self.k) % self.k]


    def isEmpty(self) -> bool:
        return not(self.size) 

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()