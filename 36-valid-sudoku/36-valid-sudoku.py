class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sqr = [set(),set(),set()]
        row = set()
        cols =[set() for _ in range(9)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":continue
            
                if board[i][j] in row: return False
                else: row.add(board[i][j])
                    
                if board[i][j] in cols[j]:return False
                else:cols[j].add(board[i][j])
                    
                if board[i][j] in sqr[j//3]: return False
                else:sqr[j//3].add(board[i][j])
            
            if i == 2 or i == 5 or i == 8:
                for s in sqr:
                    s.clear()
            row.clear()
            
        return True
        