class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        wordCount = Counter(word)
        boardCount = defaultdict(int)
        for i in range(row):
            for j in range(col):
                boardCount[board[i][j]] += 1
        for w in word:
            if boardCount[w] < wordCount[w]:
                return False
            
        
        DIR = [0,1,0,-1,0]
        is_valid = lambda r,c,i : -1 < r < row and -1 < c < col and board[r][c] == word[i]
        
    
        def dfs(r,c,i):
            if i+1 >= len(word): return True
            
            board[r][c] = -1
            for d in range(4):
                n_r = r+DIR[d]
                n_c = c + DIR[d+1]
                if is_valid(n_r,n_c,i+1):
                    if dfs(n_r,n_c,i+1):return True
            board[r][c] = word[i]
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if dfs(r,c,0): return True
        return False