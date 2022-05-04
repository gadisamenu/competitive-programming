class Node:
    def __init__(self):
        self.is_end = False
        self.next = [0]*26
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Node()
        ans = []
        def insert(word):
            temp = root
            for char in word:
                if not temp.next[ord(char)-97]:
                    temp.next[ord(char)-97] = Node()
                temp = temp.next[ord(char)-97]
            temp.is_end = True
            
        def search(word):
            ans.append([])
            temp = root
            for char in word:
                if not temp.next[ord(char)-97]:
                    return
                temp = temp.next[ord(char)-97]
            suggestions(word,temp,[])
            
        def suggestions(word,root,path:list):
            if root.is_end:
                ans[-1].append(word+"".join(path))
                
            for idx in range(len(root.next)):
                if len(ans[-1]) == 3: return
                if root.next[idx]:
                    path.append(chr(idx+97))
                    suggestions(word,root.next[idx],path)
                    path.pop()
                
        for product in products:
            insert(product)
    
        for idx in range(1,len(searchWord)+1):
            search(searchWord[:idx])
            if not ans[-1]:
                ans.extend([[] for x in range(len(searchWord)-idx)])
                break
            
        return ans
            
                    
            
                
            
                
                
            
            