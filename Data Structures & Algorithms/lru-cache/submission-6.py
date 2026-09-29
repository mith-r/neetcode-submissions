class LRUCache:

    def __init__(self, capacity: int):
        self.queue = deque()
        self.cache = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache:
            self.cache.pop(self.queue.popleft())
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)
        self.cache[key] = value

        
