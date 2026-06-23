class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        if index < 0 or self.head is None:
            return -1
        curr = self.head
        i = index
        while i > 0 :
            if curr.next == None:
                return -1
            curr = curr.next
            i -= 1
        return curr.val

        

    def addAtHead(self, val: int) -> None:
        node1 = Node(val)
        node1.next = self.head
        self.head = node1
        

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = Node(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return
        curr = self.head
        i = index - 1
        while i > 0:
            if curr == None or curr.next == None:
                return
            curr = curr.next
            i -= 1
        if curr == None: return
        node2 = Node(val)
        node1 = curr
        node3 = curr.next

        node2.next = node3
        node1.next = node2
        

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None or index < 0:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            i = index - 1
            while i > 0:
                if curr.next == None:
                    return
                curr = curr.next
                i -= 1
            if curr.next:
                curr.next = curr.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)