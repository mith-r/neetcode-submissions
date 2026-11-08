class Node:
    def __init__ (self,prev_,next_,key,val):
        self.prev_ = prev_
        self.next_ = next_

        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(prev_ = None, next_ = None, val = None, key = None)
        self.tail = Node(prev_ = None, next_ = None, val = None, key = None)

        self.tail.next_ = self.head
        self.head.prev_ = self.tail

        self.cache = {}
        self.capacity = capacity
    
    def update_position(self,node):

        #mending existing connection
        if node.next_:
            node.next_.prev_ = node.prev_
        if node.prev_:
            node.prev_.next_ = node.next_

        #pointing itself into new place
        node.prev_ = self.head.prev_
        node.next_ = self.head

        #pointing new places to it
        self.head.prev_.next_ = node
        self.head.prev_ = node
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.update_position(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.val = value

        else:
            node = Node(prev_ = None, next_ = None, val = value, key = key)
            self.cache[key] = node
        
        self.update_position(node)

        if len(self.cache) > self.capacity:
            del self.cache[self.tail.next_.key]

            self.tail.next_ = self.tail.next_.next_
            self.tail.next_.prev_ = self.tail

            
        
        
