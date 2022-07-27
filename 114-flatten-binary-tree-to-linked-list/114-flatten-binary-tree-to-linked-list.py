# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            l_tail = dfs(node.left) if node.left else None
            r_tail = dfs(node.right) if node.right else None
            
            if l_tail and r_tail:
                l_tail.right = node.right
                node.right = node.left
                node.left = None
                return r_tail
            if l_tail:
                node.right = node.left
                node.left = None
                return l_tail
            if r_tail:
                return r_tail
            return node
            
            
                
        
        if root: dfs(root)
        
        