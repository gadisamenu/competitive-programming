from sortedcontainers import SortedList

class AllOne:

    def __init__(self):
        self.freq_count = defaultdict(set)
        self.word_count = defaultdict(int)
        self.sorted_frequency = SortedList()
        

    def inc(self, key: str) -> None:
        if self.word_count[key] == 0:
            if len(self.freq_count[1]) == 0:
                self.sorted_frequency.add(1)
            self.freq_count[1].add(key)
            self.word_count[key] += 1
        else:
            if len(self.freq_count[self.word_count[key]]) == 1:
                self.sorted_frequency.discard(self.word_count[key])
            self.freq_count[self.word_count[key]].remove(key)
            self.word_count[key] += 1
            
            if len(self.freq_count[self.word_count[key]]) == 0:
                self.sorted_frequency.add(self.word_count[key])
            self.freq_count[self.word_count[key]].add(key)
            
            
    def dec(self, key: str) -> None:
        if self.word_count[key] == 1:
            if len(self.freq_count[1]) == 1:
                self.sorted_frequency.discard(1)
            self.freq_count[1].remove(key)
            self.word_count[key] -= 1
        else:
            if len(self.freq_count[self.word_count[key]]) == 1:
                self.sorted_frequency.discard(self.word_count[key])
            self.freq_count[self.word_count[key]].remove(key)
            
            self.word_count[key] -= 1
        
            if len(self.freq_count[self.word_count[key]]) == 0:
                self.sorted_frequency.add(self.word_count[key])
            self.freq_count[self.word_count[key]].add(key)
   

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
    

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()