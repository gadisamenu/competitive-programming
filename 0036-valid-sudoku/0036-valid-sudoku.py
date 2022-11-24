class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = 9
        cols= 9
        sub_box = [set(),set(),set()]
        row = set()
        col = [set() for i in range(cols)]
        for r in range(rows):
            row.clear()
            if not r%3:
                sub_box = [set(),set(),set()]
                
            for c in range(cols):
                if board[r][c] != ".":
                    if board[r][c] in row or board[r][c] in col[c] or board[r][c] in sub_box[c//3]:
                        return False
                    row.add(board[r][c])
                    col[c].add(board[r][c])
                    sub_box[c//3].add(board[r][c])
                    
        return True
                
                
        