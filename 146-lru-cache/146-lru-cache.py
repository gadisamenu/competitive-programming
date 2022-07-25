class LRUCache:

    def __init__(self, capacity: int):
        self.memory = defaultdict(int)
        self.capacity = capacity
        self.que = deque()
        self.removed = defaultdict(int)
        
    def get(self, key: int) -> int:
        if key in self.memory:
            self.que.append(key)
            self.removed[key] += 1
            return self.memory[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.memory:
            self.removed[key] += 1
        elif len(self.memory) == self.capacity:
            while self.que and self.removed[self.que[0]] > 0:
                self.removed[self.que[0]] -= 1
                self.que.popleft()
            self.memory.pop(self.que[0])
            self.que.popleft()
        self.que.append(key)
        self.memory[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)