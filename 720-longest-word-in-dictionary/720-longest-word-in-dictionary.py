class Node:
    def __init__(self):
        self.nxt = [None]*26
        self.end = False
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        def insert(word,root):
            for c in word:
                ind = ord(c) - 97
                if root.nxt[ind] == None:
                    root.nxt[ind] = Node()
                root = root.nxt[ind]
            root.end = True
        self.ans = []
        def check(root,path):
            for ind in range(len(root.nxt)):
                if root.nxt[ind] and  root.nxt[ind].end:
                    path.append(chr(97+ind))
                    if len(path) > len(self.ans):
                        self.ans = path[::]
                    check(root.nxt[ind],path)
                    path.pop()
        
        root= Node()
        for word in words:
            insert(word,root)
            
        check(root,[])
        return "".join(self.ans)
        
        
            