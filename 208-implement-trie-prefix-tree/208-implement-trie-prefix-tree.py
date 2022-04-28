class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        temp = self.root
        for char in word:
            char.lower()
            if not temp.childrens[ord(char)-97]: temp.childrens[ord(char)-97] = Node()
            temp = temp.childrens[ord(char)-97]
        temp.is_end = True

    def search(self, word: str,is_prefix:bool  = False) -> bool:
        temp = self.root
        for char in word:
            char.lower()
            if temp.childrens[ord(char)-97]:
                temp = temp.childrens[ord(char)-97]
            else:
                return False
        return True if temp.is_end or is_prefix else False
            
    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix,True)
        
class Node:
    def __init__(self):
        self.is_end = False
        self.childrens = [False]*26
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)