class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        temp = self.root
        for char in word:
            temp = temp.childrens[char]
        temp.is_end = True

    def search(self, word: str,is_prefix:bool  = False) -> bool:
        temp = self.root
        for char in word:
            if char in  temp.childrens:
                temp = temp.childrens[char]
            else:
                return False
        return True if temp.is_end or is_prefix else False
            
    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix,True)
        
class Node:
    def __init__(self):
        self.is_end = False
        self.childrens = defaultdict(Node)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)