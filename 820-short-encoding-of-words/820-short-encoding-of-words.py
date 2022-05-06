class Node:
    def __init__(self):
        self.is_end= False
        self.next = defaultdict(Node)
        
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = Node()
        length = [0]
        words.sort(key = lambda x:-len(x))
        
        def insert(word):
            temp = root
            found = True
            for ind in range(len(word)-1,-1,-1):
                if word[ind] not in temp.next:
                    found = False
                temp = temp.next[word[ind]]
                
            temp.is_end = True
            if not found:
                length[0] += len(word) + 1
        
        for word in words:
            insert(word)
            
        return length[0]
            