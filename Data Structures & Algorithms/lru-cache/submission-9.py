class Node:
    
    def __init__(self):
        self.key = None
        self.value = None

        self.nex = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()

        self.head.prev = self.tail
        self.tail.nex = self.head

        self.table = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.table:
            node = self.table[key]
            self.remove(node)
            self.front(node)
            return node.value
        else:
            return -1


    def remove(self,node):
        node.prev.nex = node.nex
        node.nex.prev = node.prev

    def front(self,node):
        node.nex = self.head
        node.prev = self.head.prev
        self.head.prev.nex = node
        self.head.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            node = self.table[key]
            self.remove(node)

        else:
            node = Node()
            node.key = key
            self.table[key] = node
        node.value = value
        self.front(node)

        if len(self.table) > self.capacity:
            rem = self.tail.nex
            self.remove(rem)
            del self.table[rem.key]
        
