class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row = len(board)
        col = len(board[0])
        answer = 0
        for r in range(row):
            for c in range(col):
                if board[r][c] == "X":
                    valid =True
                    if r + 1 < row and board[r+1][c] == "X":
                        valid = False
                    if c + 1 < col and board[r][c+1] == "X":
                        valid = False
                    if valid:
                        answer += 1
        return answer
                    