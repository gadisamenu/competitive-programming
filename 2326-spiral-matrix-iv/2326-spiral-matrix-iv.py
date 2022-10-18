# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
            
        isvalid_move = lambda r,c: -1 < r < m  and -1 < c < n and matrix[r][c] == -1
        
        matrix = [[-1 for i in range(n)] for j in range(m)]
        
        next_direction = {"up":"right","down":"left","right":"down","left":"up"}
        next_cell = {"up":(-1,0),"down":(1,0),"right":(0,1),"left":(0,-1)}
        
        self.direction = "right"
        self.head = head
        
        def fill_cell(row,col):
            if not self.head:
                return matrix
            
            matrix[row][col] = self.head.val
            self.head = self.head.next
            
            next_row = row + next_cell[self.direction][0]
            next_col = col + next_cell[self.direction][1]
            
            if not isvalid_move(next_row,next_col):
                self.direction =  next_direction[self.direction]
                next_row = row + next_cell[self.direction][0]
                next_col = col + next_cell[self.direction][1]
                
            return fill_cell(next_row,next_col)
                

        return fill_cell(0,0)
    