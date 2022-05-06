class Node:
    def __init__(self):
        self.next = defaultdict(Node)
        self.is_end = False
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = Node()
        path = []
        
        def insert(word):
            temp = root
            for char in word:
                temp = temp.next[char]
            temp.is_end = True
                
        def check():
            nonlocal root
            idx = 0
            while len(root.next) == 1:
                path.append(strs[0][idx])
                root = root.next[strs[0][idx]]
                if root.is_end: break
                idx+=1
            return "".join(path)
                
        for word in strs:
            if word:
                insert(word)
            else: return ""
            
        return check()
        