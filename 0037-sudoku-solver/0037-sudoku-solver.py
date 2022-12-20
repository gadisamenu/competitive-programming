class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        sub_boxes = [[set(),set(),set()] for _ in range(3)]
        
        empty = []
        for r in range(len(rows)):
            for c in range(len(cols)):
                if board[r][c] == ".":
                    empty.append((r,c))
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    sub_boxes[r//3][c//3].add(board[r][c])
                    
        def dp(index):
            if index == len(empty):
                return True
            row,col = empty[index]
            for num  in range(1,10):
                str_num = str(num)
                if str_num  not in rows[row] and str_num not in cols[col] and str_num not in sub_boxes[row//3][col//3]:
                
                    rows[row].add(str_num)
                    cols[col].add(str_num)
                    sub_boxes[row//3][col//3].add(str_num)
                    board[row][col] = str_num
                    if dp(index+1):
                        return True
                    board[row][col] = "."
                    rows[row].remove(str_num)
                    cols[col].remove(str_num)
                    sub_boxes[row//3][col//3].remove(str_num)
                    
            return False
        
        dp(0)
        
                    
            
            
        

        
        