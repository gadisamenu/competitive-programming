# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.time = 0
        
        def dfs(node):   
            l_dis,l_flag = dfs(node.left) if  node.left else (0,False)
            r_dis,r_flag = dfs(node.right) if node.right else (0,False)
            if l_flag:
                self.time = max(self.time,r_dis+l_dis+1)
                return 1 +l_dis,l_flag
            elif r_flag:
                self.time = max(self.time,r_dis + l_dis + 1)
                return 1 +r_dis,r_flag
            
            if node.val == start:
                self.time = max(self.time,r_dis,l_dis)
                return 0,True
            
            return max(l_dis,r_dis) +1 ,False
        
        dfs(root)
        return self.time