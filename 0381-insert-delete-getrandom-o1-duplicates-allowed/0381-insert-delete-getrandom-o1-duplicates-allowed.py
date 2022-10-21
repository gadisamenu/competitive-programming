class RandomizedCollection:

    def __init__(self):
        self.multiset = defaultdict(set)
        self.numbers = []

    def insert(self, val: int) -> bool:
        not_found = True if not val in self.multiset else False
        self.numbers.append(val)
        self.multiset[val].add(len(self.numbers)-1)
        return not_found
            
    def remove(self, val: int) -> bool:
        if val not in self.multiset:
            return False
        for index in self.multiset[val]:
            self.multiset[val].remove(index)
            if not self.multiset[val]:
                self.multiset.pop(val)
            if index != (len(self.numbers)-1):
                self.numbers[index] = self.numbers[-1]
                self.multiset[self.numbers[index]].remove(len(self.numbers)-1)
                self.multiset[self.numbers[index]].add(index)
            self.numbers.pop()
            return True
            
    def getRandom(self) -> int:
        return random.choice(self.numbers)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()