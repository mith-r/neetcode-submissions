class Node:

    def __init__(self):
        self.val = None
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.count = 0
        self.head = Node()
        self.tail = Node()

        self.head.prev = self.tail
        self.tail.next = self.head

        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.count < self.k:
            node = Node()
            node.val = value
            node.next = self.head
            node.prev = self.head.prev

            self.count += 1
            self.head.prev.next = node
            self.head.prev = node

            return True
        else:
            return False

        

    def deQueue(self) -> bool:
        if self.count > 0:
            self.tail.next = self.tail.next.next
            self.tail.next.prev = self.tail

            self.count -= 1
            return True
        else:
            return False
        

    def Rear(self) -> int:
        if self.count ==0:
            return -1
        else:
            return self.head.prev.val
        

    def Front(self) -> int:
        if self.count == 0:
            return -1
        else:
            return self.tail.next.val
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()