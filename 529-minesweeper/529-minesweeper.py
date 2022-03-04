class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row =len(board)
        col = len(board[0])
        DIR=[0,1,1,-1,-1,0,-1,1,0]
       
        isValid = lambda r,c: -1<r<row and -1 < c< col
        def dfs(ro,co):
            if board[ro][co] == "B":
                mine = 0
                for d in range(8):
                    n_r,n_c = ro+DIR[d],co+DIR[d+1]
                    if isValid(n_r,n_c) and board[n_r][n_c] == "M":
                            mine+=1       
                if mine:
                    board[ro][co] =str(mine)
                else:
                    for d in range(8):
                        n_r,n_c = ro+DIR[d],co+DIR[d+1]
                        if isValid(n_r,n_c) and board[n_r][n_c]== "E":
                            board[n_r][n_c]= "B"
                            dfs(n_r,n_c)
                            
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
        else:
            board[click[0]][click[1]] = "B"
            dfs(click[0],click[1])
        return board

    
        