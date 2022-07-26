# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        
        def dfs(node):
            left = dfs(node.left) if node.left  else 0
            right = dfs(node.right) if node.right else 0
            
            result = left + right
            
            if node == p or node == q: result += 1
            
            if self.ans == None:
                if result == 2:
                    self.ans = node
            return result
                
    
        dfs(root)
        return self.ans
   
            