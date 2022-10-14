class TrieNode():
    def __init__(self):
        self.word = None
        self.next = defaultdict(TrieNode)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def insert(word,root):
            for c in word:
                root = root.next[c]
            root.word = word
        
        def check_pref(s,root):
            if s in root.next: return root.next[s]
            return  False
        
   
        row = len(board)
        col = len(board[0])
        is_valid = lambda r,c:- 1< r < row and -1 < c < col
        boardCount = defaultdict(int)
        for i in range(row):
            for j in range(col):
                boardCount[board[i][j]] += 1
                
        trie_root = TrieNode()
        count = 0
        for word in words:
            valid = True
            wordCount = Counter(word)
            for w in word:
                if boardCount[w] < wordCount[w]: 
                    valid = False
                    break
            if valid:
                count +=1
                insert(word,trie_root)
      
        DIR = [0,-1,0,1,0]
        def dfs(r,c,root):
            t= board[r][c]
            board[r][c] = 1
            for d in range(4):
                n_r = r + DIR[d]
                n_c = c + DIR[d+1]
                if is_valid(n_r,n_c):
                    n = check_pref(board[n_r][n_c],root)
                    if n:
                        if n.word: ans.add(n.word)
                        if len(ans) < count: dfs(n_r,n_c,n)    
                        else:break
            board[r][c] = t
        
        ans = set()
        for r in range(row):
            for c in range(col):
                n = check_pref(board[r][c],trie_root)
                if n:
                    if n.word: ans.add(n.word)
                    if len(ans) < count: dfs(r,c,n)
                    else:return ans
        return ans
                
        
                
                    
                    
            
            
        