class RandomizedSet:

    def __init__(self):
        self.numbers= []
        self.index_of_numbers = {}
        
    def insert(self, val: int) -> bool:
        if val in self.index_of_numbers:
            return False
        self.numbers.append(val)
        self.index_of_numbers[val] = len(self.numbers)-1
        return True

    def remove(self, val: int) -> bool:
        if val in self.index_of_numbers:
            if self.index_of_numbers[val] != len(self.numbers)-1:
                self.numbers[self.index_of_numbers[val]] = self.numbers[-1]
                self.index_of_numbers[self.numbers[-1]]=self.index_of_numbers[val]
            self.numbers.pop()
            self.index_of_numbers.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.numbers)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()