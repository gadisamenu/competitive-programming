class Solution:

    def __init__(self, w: List[int]):
        self.numbers = list(range(len(w)))
        self.weights = w
        
    def pickIndex(self) -> int:
        return random.choices(self.numbers,weights=self.weights)[0]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()