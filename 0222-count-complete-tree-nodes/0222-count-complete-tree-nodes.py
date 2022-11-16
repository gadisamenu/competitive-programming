# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
    
        def dfs(root,left = False):
            dbth = 0
            while root:
                root = root.left if left else root.right
                dbth +=1
            return dbth
        
        left_debth = dfs(root,True)
        right_debth = dfs(root)
        
        if left_debth == right_debth:
            return 2**(left_debth) - 1
        
        answer = 2**(left_debth-1) - 1
        last  = 2**(left_debth-1)
       
        while root:
            mdl  = dfs(root.left) + 1
            last -= last//2
            if left_debth == mdl:
                answer += last
                root = root.right
            else:
                root = root.left
                
            left_debth -= 1
            right_debth -= 1
                
        return answer
            
                
    
            