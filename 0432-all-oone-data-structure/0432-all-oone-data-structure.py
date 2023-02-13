from sortedcontainers import SortedList

class AllOne:

    def __init__(self):
        self.freq_count = defaultdict(set)
        self.word_count = defaultdict(int)
        self.sorted_frequency = SortedList()
        

    def inc(self, key: str) -> None:
        if self.word_count[key]:
            self.remove_from_frequency(key)
        self.word_count[key] += 1
        self.add_to_frequency(key)
        
            
            
    def dec(self, key: str) -> None:
        self.remove_from_frequency(key)
        self.word_count[key] -= 1
        if self.word_count[key]:
            self.add_to_frequency(key)
        

    def getMaxKey(self) -> str:
        if len(self.sorted_frequency) == 0:
            return ""
        lgth = self.sorted_frequency[-1]
        return next(iter(self.freq_count[lgth]))
    

    def getMinKey(self) -> str:
        if len(self.sorted_frequency) == 0:
            return ""
        lgth = self.sorted_frequency[0]
        return next(iter(self.freq_count[lgth]))
    
    
    def remove_from_frequency(self,key):
        if len(self.freq_count[self.word_count[key]]) == 1:
            self.sorted_frequency.discard(self.word_count[key])
        self.freq_count[self.word_count[key]].remove(key)
        
    def add_to_frequency(self,key):
        if len(self.freq_count[self.word_count[key]]) == 0:
            self.sorted_frequency.add(self.word_count[key])
        self.freq_count[self.word_count[key]].add(key)


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()